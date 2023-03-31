from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_abolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=450)  # заголовок поста
    date = models.CharField(max_length=450)  # Дата
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()  # Поле нашего поста
    category = models.ForeignKey(
        'blog.Category',
        on_delete=models.CASCADE
    )

    def __str__(self):  # Метод
        return self.title


class BirdPost(models.Model):
    title = models.CharField(max_length=450)  # Заголовок поста
    date = models.CharField(max_length=450)  # Дата
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()  # Поле нашего поста

    def __str__(self):  # Метод
        return self.title


class MammalsPost(models.Model):
    title = models.CharField(max_length=450)  # Заголовок поста
    date = models.CharField(max_length=450)  # Дата
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()  # Поле нашего поста

    def __str__(self):  # Метод
        return self.title


class FishPost(models.Model):
    title = models.CharField(max_length=450)  # Заголовок поста
    date = models.CharField(max_length=450)  # Дата
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()  # Поле нашего поста

    def __str__(self):  # Метод
        return self.title
