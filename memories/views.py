from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.utils import timezone
from core.models import User
from .models import Memory, Picture, Chapter, TimelineItem
from .forms import TextForm, CommentForm, FileFieldForm
from .utils import get_exif_date_time, fix_orientation

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
def timeline(request):
    timeline_items = TimelineItem.objects.exclude(date__isnull=True).exclude(memory__is_comment_on__isnull=False).order_by('date')
    first_chapter = Chapter.objects.order_by('date')[0]
    return render(request, 'memories/timeline.html', {'timeline_items': timeline_items, 'first_chapter': first_chapter})
