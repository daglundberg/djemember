from django.contrib import admin

from .models import Text, Picture, Chapter, Milestone

admin.site.register(Text)
admin.site.register(Picture)
admin.site.register(Chapter)
admin.site.register(Milestone)
