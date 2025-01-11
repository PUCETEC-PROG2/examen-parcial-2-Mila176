
from django.contrib import admin
from .models import Movie, Actor

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'author', 'genre')  # Asegúrate de usar los nombres de campo correctos

admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)