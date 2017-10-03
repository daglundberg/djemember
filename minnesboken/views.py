from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse, redirect
from .models import Memory, Picture, Writing, CloudinaryPhoto
from random import randint
from django.utils import timezone
from .forms import MemoryForm, PictureForm, PhotoDirectForm
import datetime
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django import forms

from cloudinary.forms import cl_init_js_callbacks
from django.views.decorators.csrf import csrf_exempt
import json


cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME', ''),
    api_key=os.environ.get('CLOUDINARY_API_KEY', ''),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', '')
)


@csrf_exempt
def direct_upload_complete(request):
    form = PhotoDirectForm(request.POST)
    if form.is_valid():
        form.save()
        ret = dict(photo_id=form.instance.id)
    else:
        ret = dict(errors=form.errors)

    return HttpResponse(json.dumps(ret), content_type='application/json')


def share_a_memory(request):
    if request.user.is_authenticated and request.user.is_activated:
        context = dict(direct_form=PhotoDirectForm())
        cl_init_js_callbacks(context['direct_form'], request)
        return render(request, 'minnesboken/memories/upload_prompt.html', context)
    else:
        return render(request, '/templates/not_activated.html')

# def compose_memory(request):
#     if request.method == "POST":
#         context = dict(backend_form=PhotoDirectForm())
#         cloudinaryPhotoForm = PhotoForm(request.POST, request.FILES)
#         context['posted'] = cloudinaryPhotoForm.instance
#         if cloudinaryPhotoForm.is_valid():
#             cloudinaryPhotoForm.save()
#         memoryForm = MemoryForm(request.POST)
#         pictureForm = PictureForm(request.POST)
#         if memoryForm.is_valid():
#             if pictureForm.is_valid():
#                 memory = memoryForm.save(commit=False)
#                 memory.userprofile = UserProfile.objects.filter(user=request.user)[0]
#                 memory.pub_date = datetime.datetime.now()
#                 memory.save()

#                 picture = pictureForm.save(commit=False)
#                 picture.memory = memory
#                 picture.save()

#                 return redirect('memory_detail', memory_id=memory.pk)
#     else:
#         memoryForm = MemoryForm()
#         pictureForm = PictureForm()
#         cloudinaryPhotoForm = PhotoForm()
#     return render(request, 'minnesboken/memories/compose_memory.html',
# {'memoryForm': memoryForm, 'pictureForm': pictureForm, 'cloudinaryPhotoForm': cloudinaryPhotoForm})


def landingpage(request):
    public_writings = Writing.objects.filter(is_featured_publicly=True)
    public_pictures = Picture.objects.filter(is_featured_publicly=True)
    public_memories = Memory.objects.filter(is_featured_publicly=True)

    if public_writings.count() > 0:
        random_writing = public_writings[randint(0, public_writings.count() - 1)]
    else:
        random_writing = "No public writings."

    if public_pictures.count() > 0:
        random_picture = public_pictures[randint(0, Picture.objects.count() - 1)]
    else:
        random_picture = "No public pictures."

    if public_memories.count() > 0:
        random_memory = public_memories[randint(0, Memory.objects.count() - 1)]
    else:
        random_memory = "No public memories."

    return render(request, 'minnesboken/landingpage.html', {
                           'random_picture': random_picture,
                           'random_memory': random_memory,
                           'random_writing': random_writing})


def timeline(request):
    timeline_memories_list = Memory.objects.filter(is_on_timeline=True).order_by('timeline_date')
    return render(request, 'minnesboken/memories/timeline.html', {'timeline_memories_list': timeline_memories_list, })


def memories(request):
    latest_memories_list = Memory.objects.filter(is_on_timeline=False).order_by('-pub_date')[:5]
    # latest_memories_list = Memory.objects.order_by
    # pics = get_list_or_404(UserProfile)
    context = {'latest_memories_list': latest_memories_list}
    return render(request, 'minnesboken/memories/memories.html', context)


def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    return render(request, 'minnesboken/memories/memory_detail.html', {'memory': memory})


def pictures(request):
    latest_pictures_list = Picture.objects.order_by('-date_taken')[:5]
    context = {'latest_pictures_list': latest_pictures_list}
    return render(request, 'minnesboken/pictures/pictures.html', context)


def picture_detail(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    return render(request, 'minnesboken/pictures/picture_detail.html', {'picture': picture})


def writings(request):
    writings_list = Writing.objects.all()
    return render(request, 'minnesboken/writings/writings.html', {'writings_list': writings_list})


def writing_detail(request, writing_id):
    writing = get_object_or_404(Writing, pk=writing_id)
    return render(request, 'minnesboken/writings/writing_detail.html', {'writing': writing})


def post_memory(request):  # TODO: Have some fun here
    if request.user.is_authenticated() is False:
        return HttpResponseForbidden()
    else:

        # TODO: the following should throw an exception if theres no UserProfile assigned to current user, because this could happen :/

        mymemory = Memory(userprofile=request.user, memory_text=request.POST['text'], pub_date=timezone.now())
        mymemory.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('memories'))
