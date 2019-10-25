from django.contrib import admin
from .models import Profile, Rating, Project

# Register your models here.
admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(Project)