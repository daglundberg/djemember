# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Picture, Memory


class MemoryTimelineForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ('text', 'timeline_date')
        labels = {
            "text": "Minnestext",
            "timeline_date": "Tidpunkt för minnet"}


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ('text', )


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ('picture_text', 'picture_location', 'date_taken')
        labels = {
            "picture_text": "Kortfattad undertext",
            "picture_location": "Plats där bilden togs",
            "date_taken": "Datum när bilden togs"}
