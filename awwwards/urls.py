from django.conf.urls import url,include
from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
# from .views import ImageCreateView

# Template URLS
app_name = 'awwwards'

urlpatterns = [
    path('', main_views.index , name = 'index'),
    path('register/', main_views.signup, name='signup'),
    path('new/', main_views.newproject, name = "newproject"),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)