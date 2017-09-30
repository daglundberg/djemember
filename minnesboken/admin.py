from django.contrib import admin

from .models import Memory, Picture, Writing, UserProfile

admin.site.register(Memory)
admin.site.register(Picture)
admin.site.register(Writing)
admin.site.register(UserProfile)
