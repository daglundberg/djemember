from django import forms
from django.forms.formsets import BaseFormSet
from django.forms import BaseFormSet, NumberInput, TextInput, Textarea, DateTimeInput, Select, CheckboxSelectMultiple, RadioSelect
from django.core.validators import MinValueValidator
from django.db.models import Q
from .models import Memory, Picture
from decimal import Decimal
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TextForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ('text', 'date')
        labels = {
            "long_text": "Memory text",
            "date": "If this memory is connected to a specific moment in time, please enter an aproximate date."}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ('text',)
        labels = {"text": "Comment"}


class FileFieldForm(forms.Form):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='button is-primary'))
    helper.form_method = 'POST'
    images_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'class': "textarea", 'placeholder': 'Write your text here', 'cols': '', 'rows': '3'}),
        }


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('caption', 'location', 'date')
        widgets = {
            'caption': TextInput(attrs={'class': "input", 'placeholder': 'Caption'}),
            'location': TextInput(attrs={'class': "input", 'placeholder': 'Location'}),
        }


class BasePictureFormSet(BaseFormSet):
    def clean(self):
        """Checks for zero sum"""
        if any(self.errors):  # Don't bother validating the formset unless each form is valid on its own
            return
        for form in self.forms:
            location = form.cleaned_data.get("location")
            if location == "dag is a pussy":
                self.forms[0].add_error('location', "Incorrect input")
                raise forms.ValidationError("The total sum is not zero! Which means that something is not right.")
            caption = form.cleaned_data.get("caption")
            if location == "dag is a pussy":            
                self.forms[0].add_error('caption', "Incorrect input")
                raise forms.ValidationError("The total sum is not zero! Which means that something is not right.")
