from django.conf import settings
from django.conf.urls import static
from django.urls import path
from mods.views import *

app_name = "mods"

urlpatterns = [
    path('', LyricsView, name='home'),
    path('lyrics/', LyricsView, name='lyrics'),
    path('edit/<slug:slug>', UpdateLyricView.as_view(), name='edit'),
    path('create/', AddLyricView.as_view(), name='create'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    
]