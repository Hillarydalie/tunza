from rest_framework import serializers
from .models import Profile, Project

class profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id','user', 'profile_pic', 'bio')

class projectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id','user', 'project_name', 'project_caption', 'published_date', 'project_image')