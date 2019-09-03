from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse, redirect
from .models import Memory, Picture, Chapter
from core.models import User
from django.utils import timezone
#from .forms import MemoryForm


@login_required
def memories(request):
    memories = Memory.objects.all().order_by('-pub_date')[:5]
    context = {'memories': memories}
    return render(request, 'memories/memories.html', context)


@login_required
def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    return render(request, 'memories/memory_detail.html', {'memory': memory})


# @login_required
# def post_memory(request):
#     if request.method == "POST":
#         form = MemoryForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.pub_date = timezone.now()
#             post.text = request.POST['text']
#             if (form.data.get('timeline_date', False)):
#                 post.timeline_date = request.POST['timeline_date']
#             post.save()
#             return redirect('memories')
#     else:
#         form = MemoryForm()
#     return render(request, 'memories/post_memory.html', {'form': form})


# TODO: Improve this ugly code!! Currently highly inefficient. (It's looping through the same memories many times for instance..)
# The idea is to combine all the memories and chapters in to one sorted list instead of trying to sort them in the template
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
