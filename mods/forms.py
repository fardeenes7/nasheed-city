from django import forms
from ckeditor.fields import RichTextField
from django.db.models import fields
from embed_video.fields import EmbedVideoField
from lyrics.models import Lyric, Profile

class LyricForm(forms.ModelForm):
    class Meta:
        model = Lyric
        fields = ('name', 'singer', 'language', 'youtube_link', 'date', 'lyrics', 'user')
        CHOICES=[
        ('arabic', 'Arabic'),
        ('bangla', 'Bangla'),
        ('english', 'English'),
        ('urdu', 'Urdu'),
        ('mixed', 'Mixed'),
        ('other', 'Other')
    ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'singer': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'youtube_link': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'language' : forms.Select(attrs={'class': 'form-control mb-3'}),
            'date': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'lyrics': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'user': forms.TextInput(attrs={'class': 'form-control mb-3', 'readonly': 'readonly'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'display_name', 'facebook', 'youtube', 'profile_picture', 'bio')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control mb-3', 'readonly': 'readonly'}),
            'display_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'youtube': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }