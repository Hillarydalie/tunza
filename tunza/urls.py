"""tunza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from awwwards import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/',auth_views.LoginView.as_view(template_name = 'user/login.html'),name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name = 'user/logout.html'),name='logout'),
    url(r'', include('awwwards.urls')),
    path('profiler/', views.profileList.as_view()),
    path('projector/', views.projectList.as_view()),
]
