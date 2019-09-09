import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, Http404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Memory, Picture
from django.forms import formset_factory
from .forms import MemoryForm, PictureForm, BasePictureFormSet
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView


# TODO: Potential problem below where picture wont get saved bc cleaned_data returns false
# TODO: ..and memory still gets saved bc it doesnt wait for the picture
@login_required
def megaform(request):
    unpublished_pictures = Picture.objects.filter(user=request.user).filter(memory__isnull=True)
    pic_urls = list()
    for pic in unpublished_pictures:
        pic_urls.append(pic.image.url)
    PictureFormSet = formset_factory(PictureForm, formset=BasePictureFormSet, extra=0, min_num=0, validate_min=True)
    if request.method == 'POST':
        pass
        data = request.POST or None
        formset = PictureFormSet(data=data)
        form = MemoryForm(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
             memory = form.save(commit=False)
             memory.user = request.user
             memory.save()
             for inline_form, pic in zip(formset, unpublished_pictures):
                 if inline_form.cleaned_data:
                     picture = inline_form.save(commit=False)
                     pic.caption = picture.caption
                     pic.date = picture.date
                     pic.location = picture.location
                     pic.memory = memory
                     pic.save()
             messages.success(request, 'Saved "' + memory.text + '"" !')
             return HttpResponseRedirect(request.path_info)
    else:
        formset = PictureFormSet(initial=unpublished_pictures.values())
        form = MemoryForm()

    return render(request, 'megaform.html', {'form': form, 'formset': formset, 'pic_urls': pic_urls})
