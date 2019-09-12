from django.contrib import admin

from .models import TimelineItem, Memory, Picture, Chapter, Milestone, Quote

admin.site.register(TimelineItem)
admin.site.register(Memory)
admin.site.register(Picture)
admin.site.register(Chapter)
admin.site.register(Milestone)
admin.site.register(Quote)
