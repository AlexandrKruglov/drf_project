from django.db import models

from users.models import NULLABLE, User


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


class Payments(models.Model):
    CASH = 'наличные'
    TRANSFER = 'перевод'

    PAY_METHOD = [
        (CASH, 'наличные'),
        (TRANSFER, 'перевод'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date_pay = models.DateField(verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', **NULLABLE)
    summ = models.PositiveIntegerField(verbose_name='сумма оплаты')
    pay_method = models.CharField(
        max_length=50,
        choices=PAY_METHOD,
        default=CASH,
        verbose_name="способ оплаты")

    def __str__(self):
        return f'{self.user} - {self.course if self.course else self.lesson}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
