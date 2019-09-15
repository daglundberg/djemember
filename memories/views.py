from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Picture, Chapter, Album
from .forms import FileFieldForm
from .utils import get_exif_date_time, fix_orientation, get_exif_gps_data


@login_required
def post_list(request):
    posts = Post.objects.order_by('-pub_date')[:15]
    return render(request, 'memories/post_list.html', {'posts': posts})


@login_required
def post_detail(request, text_id):
    post = get_object_or_404(Post, pk=text_id)
    return render(request, 'memories/post_detail.html', {'post': post})


@login_required
def timeline(request):
    timeline_items = Post.objects.exclude(timeline_date__isnull=True).order_by('timeline_date')
    try:
        first_chapter = Chapter.objects.order_by('timeline_date')[0]
    except:
        first_chapter = "No chapter created"
    return render(request, 'memories/timeline.html', {'timeline_items': timeline_items, 'first_chapter': first_chapter})


@login_required
def images_upload(request):
    if request.method == "POST":
        form = FileFieldForm(request.POST, request.FILES)
        files = request.FILES.getlist('images_field')
        if form.is_valid():
            for f in files:
                print(f)
                p = Picture()
                p.user = request.user
                p.image = f
                p.save()
                date = get_exif_date_time(p.image.path)
                gpsdata = get_exif_gps_data(p.image.path)
                if date is not None:
                    p.date_taken = date
                if gpsdata is not None:
                    p.gps_data = gpsdata
                p.save()
                fix_orientation(p.image.path)
            return redirect('album_create')
    else:
        form = FileFieldForm()
    return render(request, 'utilities/_generic_form.html', {'form': form})
