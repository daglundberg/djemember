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
    