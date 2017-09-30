# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from cloudinary.forms import CloudinaryJsFileField
from .models import Picture, Memory, CloudinaryPhoto


class MemoryForm(forms.ModelForm):

    class Meta:
        model = Memory
        fields = ('text',)


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ('picture_text', 'picture_location', 'date_taken')
        labels = {
            "picture_text": "Kortfattad undertext",
            "picture_location": "Plats där bilden togs",
            "date_taken": "Datum när bilden togs"}


class PhotoDirectForm(ModelForm):

    class Meta:
        model = CloudinaryPhoto
        fields = ('image',)
    image = CloudinaryJsFileField()
