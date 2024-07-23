from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название курса')
    image = models.ImageField(upload_to='materials/image', verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('name',)


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название урока')
    image = models.ImageField(upload_to='materials/image', verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    link = models.CharField(max_length=100, verbose_name='ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('name',)
