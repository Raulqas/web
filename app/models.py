from django.db import models
from datetime import datetime
from django.contrib.auth.models import User  # вверху файла


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now, db_index=True, verbose_name="Опубликована")
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Автор"
    )
    image = models.ImageField(upload_to="blog_images/", blank=True, verbose_name="Изображение")  # 🔥 новое поле

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blogpost', args=[str(self.id)])

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"


class Comment(models.Model):
    text = models.TextField(verbose_name="Комментарий")
    date = models.DateTimeField(verbose_name="Дата комментария")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    post = models.ForeignKey('Blog', on_delete=models.CASCADE, verbose_name="Статья")

    def __str__(self):
        return f"Комментарий от {self.author.username} к '{self.post.title}'"
