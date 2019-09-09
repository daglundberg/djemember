from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.utils import timezone
from core.models import User
from datetime import datetime
from .models import Memory, Picture, Chapter, TimelineItem
from .forms import TextForm, CommentForm, FileFieldForm
from .utils import get_exif_date_time, fix_orientation, get_exif_gps_data


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
                    p.date = date
                if gpsdata is not None:
                	p.gps_data = gpsdata
                p.save()
                fix_orientation(p.image.path)
            return redirect('create-image-post')
    else:
        form = FileFieldForm()
    return render(request, 'memories/post_memory.html', {'form': form})


@login_required
def create_image_post(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        formset = PictureFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save

            for f in formset:
                try:
                    p = Picture()
                    p.memory = memory
                    p.caption = f.cleaned_data['caption']
                    p.save()
                except:
                    print("An exception occurred") 
            return redirect('create-image-post')
    else:
        form = TextForm()
        formset = ""
    return render(request, 'memories/test.html', {'form': form, 'formset': formset})


@login_required
def test(request):
    if request.method == "POST":
        if True: #Implement some form validation
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save

            for f in formset:
                try:
                    p = Picture()
                    p.memory = memory
                    p.caption = f.cleaned_data['caption']
                    p.save()
                except:
                    print("An exception occurred") 
            return redirect('create-image-post')
    else:
        pictures = Picture.objects.filter(user=request.user).filter(memory__isnull=True)
    return render(request, 'memories/test2.html', {'pictures': pictures})


@login_required
def testy(request):
    if request.method == "POST":
        pass
    else:
        pictures = Picture.objects.filter(user=request.user).filter(memory__isnull=True)
    return render(request, 'memories/test2.html', {'pictures': pictures})
