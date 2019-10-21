from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save

# This is ssthe profile model here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profilepic/', blank=True, default='default.png')
    bio = models.CharField(max_length=140)
    contactinfo = models.CharField(max_length=12)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender = User) 
    def create_profile(instance,sender,created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender= User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

# This is the project model
class Project(models.Model):
    project_name = models.CharField(max_length = 100, blank=True)
    project_caption = models.TextField()
    project_image = models.ImageField(upload_to="projectpics/", blank=True)
    project_url = models.URLField(max_length=200)
    published_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name= 'likes', blank=True)

    @classmethod
    def save_project(self):
        self.save()

    @classmethod
    def delete_project(self):
        self.delete()
