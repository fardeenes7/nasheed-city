from django.conf import settings
from django.conf.urls import static
from django.urls import path
from lyrics.views import *

app_name = "lyrics"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('search/', SearchView, name="search"),
    path('random/', RandomView, name="random"),
    path('blog/', BlogMain.as_view(), name="blog"),
    path('about/', AboutView, name="about"),
    path('contact/', ContactView, name="contact"),
    path('lyric/<slug:slug>', LyricView.as_view(), name="single_lyric"),
    path('<slug:language>/', LanguageView, name="language"),
    
]