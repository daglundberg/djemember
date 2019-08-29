from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse, redirect
from .models import Memory, Picture
from random import randint
from django.utils import timezone
from .forms import MemoryForm


@login_required
def memories(request):
    latest_memories_list = Memory.objects.exclude(timeline_date__isnull=False).order_by('-pub_date')[:5]
    # latest_memories_list = Memory.objects.order_by
    # pics = get_list_or_404(UserProfile)
    context = {'latest_memories_list': latest_memories_list}
    return render(request, 'minnesboken/memories/memories.html', context)


@login_required
def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    return render(request, 'minnesboken/memories/memory_detail.html', {'memory': memory})


# @login_required
# def create_post(request):
#     if request.method == "POST":
#         form = MemoryForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.userprofile = request.user
#             post.pub_date = timezone.now()
#             post.text = request.POST['text']
#             if (form.data.get('timeline_date', False)):
#                 post.timeline_date = request.POST['timeline_date']
#             post.save()
#             return redirect('timeline')
#     else:
#         form = MemoryForm()
#     return render(request, 'minnesboken/memories/create_post.html', {'form': form})


# @login_required
# def post_memory(request):  # TODO: Have some fun here
#     mymemory = Memory(userprofile=request.user, memory_text=request.POST['text'], pub_date=timezone.now())
#     mymemory.save()
#     # Always return an HttpResponseRedirect after successfully dealing
#     # with POST data. This prevents data from being posted twice if a
#     # user hits the Back button.
#     return HttpResponseRedirect(reverse('memories'))


# @login_required
# def landingpage(request):
#     public_pictures = Picture.objects.filter(is_featured_publicly=True)
#     public_memories = Memory.objects.filter(is_featured_publicly=True)

#     if public_pictures.count() > 0:
#         random_picture = public_pictures[randint(0, public_pictures.count() - 1)]
#     else:
#         random_picture = "No public pictures."

#     if public_memories.count() > 0:
#         random_memory = public_memories[randint(0, public_memories.count() - 1)]
#     else:
#         random_memory = "No public memories."

#     return render(request, 'minnesboken/landingpage.html', {
#                            'random_picture': random_picture,
#                            'random_memory': random_memory})


# @login_required
# def timeline(request):
#     timeline_memories_list = Memory.objects.exclude(timeline_date__isnull=True).order_by('timeline_date')
#     return render(request, 'minnesboken/memories/timeline.html', {'timeline_memories_list': timeline_memories_list, })


# @login_required
# def pictures(request):
#     latest_pictures_list = Picture.objects.order_by('-date_taken')[:5]
#     context = {'latest_pictures_list': latest_pictures_list}
#     return render(request, 'minnesboken/pictures/pictures.html', context)


# @login_required
# def picture_detail(request, picture_id):
#     picture = get_object_or_404(Picture, pk=picture_id)
#     return render(request, 'minnesboken/pictures/picture_detail.html', {'picture': picture})
