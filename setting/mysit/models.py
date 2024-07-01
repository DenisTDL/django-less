from django.db import models


class Task(models.Model):
    pole_1 = models.CharField('Введите текст', max_length=30)
    pole_2 = models.TextField('Пояснение')


    def __str__(self):
        return self.pole_1



    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
