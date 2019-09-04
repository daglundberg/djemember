from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse, redirect
from .models import Memory, Picture, Chapter, Text
from core.models import User
from django.utils import timezone
from .forms import TextForm, PictureForm


@login_required
def memories(request):
    memories = Text.objects.all().order_by('-pub_date')[:15]
    context = {'memories': memories}
    return render(request, 'memories/memories.html', context)


@login_required
def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    return render(request, 'memories/memory_detail.html', {'memory': memory})


@login_required
def post_text(request):
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
    memories = Memory.objects.exclude(date__isnull=True).order_by('date')
    return render(request, 'memories/timeline.html', {'memories': memories})


# @login_required
# def pictures(request):
#     latest_pictures_list = Picture.objects.order_by('-date_taken')[:5]
#     context = {'latest_pictures_list': latest_pictures_list}
#     return render(request, 'pictures/pictures.html', context)


# @login_required
# def picture_detail(request, picture_id):
#     picture = get_object_or_404(Picture, pk=picture_id)
#     return render(request, 'pictures/picture_detail.html', {'picture': picture})
