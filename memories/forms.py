from django import forms
from .models import Memory #, Picture,


class MemoryForm(forms.ModelForm):
    timeline_date = forms.DateField(required=False)

    class Meta:
        model = Memory
        fields = ('text', 'timeline_date')
        labels = {
            "text": "Memory text",
            "timeline_date": "If this memory is connected to a specific moment in time, please enter an aproximate date for this memory."}


# class PictureForm(forms.ModelForm):
#     class Meta:
#         model = Picture
#         fields = ('picture_text', 'picture_location', 'date_taken')
#         labels = {
#             "picture_text": "Brief caption",
#             "picture_location": "Place where picture was taken",
#             "date_taken": "Date when picture was taken"}
