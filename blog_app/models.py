from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    short_description = models.TextField(max_length=150, verbose_name='Краткое описание статьи')
    full_description = models.TextField(verbose_name='Полное описание статьи')
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/articles', blank=True, null=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='category')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'








