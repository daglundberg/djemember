from django.contrib import admin

from .models import Post, Picture, Album, Chapter, Milestone, Quote

admin.site.register(Post)
admin.site.register(Picture)
admin.site.register(Album)
admin.site.register(Chapter)
admin.site.register(Milestone)
admin.site.register(Quote)
