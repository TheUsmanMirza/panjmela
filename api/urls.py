from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('get_videos/', views.VideoDetailView.as_view(), name='get_videos'),
    path('add_videos/', views.AddVideo.as_view(), name='add_videos'),
    path('validate_user/', views.validate_user, name='validate_username'),
    url(r'^$', views.login, name='login'),
    url(r'^index$', views.index, name='index')
]