from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.utils import timezone
from .models import Post, Picture
from .forms import TextForm, CommentForm, PictureForm, BasePictureFormSet, AlbumForm


@login_required
def post_create(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('landingpage')
    else:
        form = TextForm()
    return render(request, 'memories/post_create.html', {'form': form})


@login_required
def comment_create(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.is_comment_on = Post.objects.get(pk=post_id)
            comment.pub_date = timezone.now()
            comment.save()
            return redirect('timeline')
    else:
        form = CommentForm()
        post = Post.objects.get(pk=post_id)
    return render(request, 'memories/comment_create.html', {'form': form, 'post': post})


# TODO: Potential problem below where picture wont get saved bc cleaned_data returns false
# TODO: ..and text still gets saved bc it doesnt wait for the picture
@login_required
def album_create(request):
    unpublished_pictures = Picture.objects.filter(user=request.user).filter(timeline_date__isnull=True).filter(is_in_album__isnull=True)
    pic_urls = list()
    for pic in unpublished_pictures:
        pic_urls.append(pic.image.url)
    PictureFormSet = formset_factory(PictureForm, formset=BasePictureFormSet, extra=0, min_num=0, validate_min=True)
    if request.method == 'POST':
        data = request.POST or None
        formset = PictureFormSet(data=data)
        form = AlbumForm(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            for inline_form, pic in zip(formset, unpublished_pictures):
                if inline_form.cleaned_data:
                    picture = inline_form.save(commit=False)
                    pic.text = picture.text
                    pic.date_taken = picture.date_taken
                    pic.location = picture.location
                    pic.is_in_album = album
                    pic.save()
            messages.success(request, 'Saved "' + album.text + '"" !')
            return redirect('timeline')
    else:
        formset = PictureFormSet(initial=unpublished_pictures.values())
        form = AlbumForm()

    return render(request, 'memories/album_create.html', {'form': form, 'formset': formset, 'pic_urls': pic_urls})


# @login_required
# def test(request):
#     if request.method == "POST":
#         if True:  # Implement some form validation
#             text = form.save(commit=False)
#             text.user = request.user
#             text.save

#             for f in formset:
#                 try:
#                     p = Picture()
#                     p.text = text
#                     p.caption = f.cleaned_data['caption']
#                     p.save()
#                 except:
#                     print("An exception occurred")
#             return redirect('create-image-post')
#     else:
#         pictures = Picture.objects.filter(user=request.user).filter(text__isnull=True)
#     return render(request, 'memories/test2.html', {'pictures': pictures})
