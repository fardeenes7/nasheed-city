from django.contrib import admin
from .models import Profile, Lyric, Blog
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('display_name',)


class LyricAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'language',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Lyric, LyricAdmin)
admin.site.register(Blog)
