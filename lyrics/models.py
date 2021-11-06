from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from django.utils.timezone import datetime
from embed_video.fields import EmbedVideoField
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    display_name = models.TextField(max_length=20)
    facebook = models.TextField(null=True, blank=True)
    youtube = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('mods:home')

class Lyric(models.Model):
    CHOICES=[
        ('arabic', 'Arabic'),
        ('bangla', 'Bangla'),
        ('english', 'English'),
        ('urdu', 'Urdu'),
        ('mixed', 'Mixed'),
        ('other', 'Other')
    ]
    name = models.CharField(max_length=100)
    singer = models.CharField(max_length=20, default="Unknown")
    lyrics = RichTextField(blank = True, null = True)
    youtube_link = EmbedVideoField()
    user = models.ForeignKey('Profile', on_delete=CASCADE)
    language = models.CharField(choices = CHOICES, max_length=10, default='Other')
    date = models.DateField(default=datetime.today, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" +self.singer)
        super(Lyric, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mods:home')

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Profile', on_delete=CASCADE)
    post = RichTextField(blank = True, null = True)
    image = models.ImageField(blank=True, null=True)
    date = models.DateField(default=datetime.today)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title+ "-" + self.author)
        super(Blog, self).save(*args, **kwargs)