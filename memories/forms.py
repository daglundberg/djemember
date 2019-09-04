from django import forms
from .models import Memory, Text, Picture
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ('long_text', 'date')
        labels = {
            "long_text": "Memory text",
            "date": "If this memory is connected to a specific moment in time, please enter an aproximate date."}


class PictureForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='button is-primary'))
    helper.form_method = 'POST'
    date = forms.DateField(required=False)
    image = forms.ImageField(required=True)

    class Meta:
        model = Picture
        fields = ('date', 'caption', 'location', 'image')
        labels = {
            "date": "If this memory is connected to a specific moment in time, please enter an aproximate date."}



# class PictureForm(forms.ModelForm):
#     class Meta:
#         model = Picture
#         fields = ('picture_text', 'picture_location', 'date_taken')
#         labels = {
#             "picture_text": "Brief caption",
#             "picture_location": "Place where picture was taken",
#             "date_taken": "Date when picture was taken"}
