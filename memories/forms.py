from django import forms
from django.forms.formsets import BaseFormSet
from django.forms import TextInput, Textarea
from .models import Post, Picture, Comment, Album
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TextForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='button is-primary'))
    helper.form_method = 'POST'

    class Meta:
        model = Post
        fields = ('text', 'timeline_date',)
        widgets = {
            'text': Textarea(attrs={'class': "textarea", 'placeholder': 'Write your text here', 'cols': '', 'rows': '3'}),
        }


class AlbumForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='button is-primary'))
    helper.form_method = 'POST'

    class Meta:
        model = Album
        fields = ('text', 'timeline_date',)
        widgets = {
            'text': Textarea(attrs={'class': "textarea", 'placeholder': 'Write your text here', 'cols': '', 'rows': '3'}),
        }


class CommentForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='button is-primary'))
    helper.form_method = 'POST'

    class Meta:
        model = Comment
        fields = ('text',)
        labels = {"text": "Comment"}


class FileFieldForm(forms.Form):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='button is-primary'))
    helper.form_method = 'POST'
    images_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('text', 'location', 'date_taken')
        widgets = {
            'text': TextInput(attrs={'class': "input", 'placeholder': 'Caption'}),
            'location': TextInput(attrs={'class': "input", 'placeholder': 'Location'}),
        }


class BasePictureFormSet(BaseFormSet):
    def clean(self):
        """Checks for zero sum"""
        if any(self.errors):  # Don't bother validating the formset unless each form is valid on its own
            return
        for form in self.forms:  # TODO: This validation is literally nonsense.. remember to make something real
            location = form.cleaned_data.get("location")
            if location == "some string":
                self.forms[0].add_error('location', "Incorrect input")
                raise forms.ValidationError("The total sum is not zero! Which means that something is not right.")
            caption = form.cleaned_data.get("caption")
            if caption == "some string":
                self.forms[0].add_error('caption', "Incorrect input")
                raise forms.ValidationError("The total sum is not zero! Which means that something is not right.")
