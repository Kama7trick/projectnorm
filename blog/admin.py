from django.contrib import admin
from .models import *

admin.site.register(Post)  # Регистрация модели нашего поста
admin.site.register(BirdPost)
admin.site.register(MammalsPost)
admin.site.register(FishPost)
admin.site.register(Category)