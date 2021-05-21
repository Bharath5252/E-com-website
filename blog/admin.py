from django.contrib import admin
from .models import Level1, Level2, Level3, Level4, post

admin.site.register(post)
admin.site.register(Level1)
admin.site.register(Level2)
admin.site.register(Level3)
admin.site.register(Level4)