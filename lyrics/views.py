from django.shortcuts import render
from .models import Lyric, Blog, Profile
from django.views.generic import ListView, DetailView
from django.db.models import Max
import random
# Create your views here.

class LyricView(DetailView):
    model = Lyric
    template_name = 'single_lyric.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LyricView, self).get_context_data(*args, **kwargs)
        context['suggestion'] = Lyric.objects.filter().order_by('-date')[:5]

        return context


class IndexView(ListView):
    model = Lyric
    queryset = Lyric.objects.order_by('-date')[:15]
    template_name = 'index.html'

class BlogMain(ListView):
    model = Blog
    template_name = 'blog.html'

class BlogView(DetailView):
    model = Blog
    template_name = 'single_blog.html'
    

def LanguageView(request, language):
    lang = language
    lyric = Lyric.objects.filter(language=language).order_by('-date')[:15]
    return render(request, 'language.html', {'lyrics': lyric, 'language': lang})


def error404(request, exception):
    return render(request, '404.html')

def SearchView(request):
    if request.method == 'POST':
        query = request.POST['search']
        lyric = Lyric.objects.filter(name__contains=query)
        return render(request, 'search.html', {'search':query, 'lyrics': lyric})
    else:
        return render(request, 'search.html')

def AboutView(request):
    lyrics = Lyric.objects.count()
    mods = Profile.objects.count()
    blogs = Blog.objects.count()
    
    return render(request, 'about.html', {'lyrics':lyrics, 'mods':mods, 'blogs':blogs})

def ContactView(request):
    return render(request, 'contact.html')

def RandomView(request):
    max_id = Lyric.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    random_lyrics = Lyric.objects.filter(pk=pk).first()
    suggestion = Lyric.objects.filter().order_by('-date')[:5]
    return render(request, 'random.html', {'lyric': random_lyrics, 'suggestion': suggestion})