from django.db.models import fields
from django.shortcuts import render
from lyrics.models import Lyric, Profile
from django.contrib.auth.decorators import login_required
from .forms import LyricForm, ProfileForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
def LoginView(request):
    return render(request, 'login.html')


@login_required()
def LyricsView(request):
    profile = Profile.objects.filter(user=request.user)[0]
    lyrics = Lyric.objects.filter(user=profile)
    return render(request, 'mods/lyrics.html', {'profile': profile, 'lyrics': lyrics})
    

class UpdateLyricView(LoginRequiredMixin, UpdateView):
    model = Lyric
    template_name = 'mods/edit.html'
    form_class = LyricForm
    #fields =  ['name', 'singer', 'lyrics', 'language', 'youtube_link', 'user']
    def get_context_data(self, *args, **kwargs):
        context = super(UpdateLyricView, self).get_context_data(*args, **kwargs)
        context['profile'] = Profile.objects.filter(user=self.request.user)[0]
        context['lyrics'] = Lyric.objects.filter(user=context['profile'])

        return context

class DeleteLyricView(LoginRequiredMixin, DeleteView):
    model = Lyric
    template_name = 'mods/delete.html'
    form_class = LyricForm
    success_url = reverse_lazy('mods:home')
    #fields =  ['name', 'singer', 'lyrics', 'language', 'youtube_link', 'user']
    def get_context_data(self, *args, **kwargs):
        context = super(DeleteLyricView, self).get_context_data(*args, **kwargs)
        context['profile'] = Profile.objects.filter(user=self.request.user)[0]
        context['lyrics'] = Lyric.objects.filter(user=context['profile'])

        return context




class AddLyricView(LoginRequiredMixin, CreateView):
    model = Lyric
    template_name = 'mods/create.html'
    form_class = LyricForm
    #fields =  ['name', 'singer', 'lyrics', 'language', 'youtube_link', 'user']
    def get_context_data(self, *args, **kwargs):
        context = super(CreateView, self).get_context_data(*args, **kwargs)
        context['profile'] = Profile.objects.filter(user=self.request.user)[0]
        context['lyrics'] = Lyric.objects.filter(user=context['profile'])

        return context
    
class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'mods/profile.html'
    form_class = ProfileForm
    #fields =  ['name', 'singer', 'lyrics', 'language', 'youtube_link', 'user']
    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['profile'] = Profile.objects.filter(user=self.request.user)[0]
        context['lyrics'] = Lyric.objects.filter(user=context['profile'])

        return context