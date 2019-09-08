from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse, redirect
from .models import Memory, Picture, Chapter, TimelineItem
from core.models import User
from django.utils import timezone
from .forms import TextForm, PictureForm, CommentForm


@login_required
def memories(request):
    memories = Memory.objects.exclude(is_comment_on__isnull=False).order_by('-pub_date')[:15]
    context = {'memories': memories}
    return render(request, 'memories/memories.html', context)


@login_required
def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    return render(request, 'memories/memory_detail.html', {'memory': memory})


@login_required
def post_memory(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('memories')
    else:
        form = TextForm()
    return render(request, 'memories/post_memory.html', {'form': form})


@login_required
def post_comment(request, timeline_item_id):
    comments = ""
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.is_comment_on = TimelineItem.objects.get(pk=timeline_item_id)
            post.pub_date = timezone.now()
            post.save()
            return redirect('timeline')
    else:
        form = CommentForm()
        comments = Memory.objects.filter(is_comment_on=timeline_item_id)
    return render(request, 'memories/post_comment.html', {'form': form, 'comments': comments})


@login_required
def post_picture(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('memories')
    else:
        form = PictureForm()
    return render(request, 'memories/post_memory.html', {'form': form})


@login_required
def timeline(request):
    timeline_items = TimelineItem.objects.exclude(date__isnull=True).exclude(memory__is_comment_on__isnull=False).order_by('date')
    first_chapter = Chapter.objects.order_by('date')[0]
    return render(request, 'memories/timeline.html', {'timeline_items': timeline_items, 'first_chapter': first_chapter})


# @login_required
# def pictures(request):
#     latest_pictures_list = Picture.objects.order_by('-date_taken')[:5]
#     context = {'latest_pictures_list': latest_pictures_list}
#     return render(request, 'pictures/pictures.html', context)


# @login_required
# def picture_detail(request, picture_id):
#     picture = get_object_or_404(Picture, pk=picture_id)
#     return render(request, 'pictures/picture_detail.html', {'picture': picture})
