from django.db import models


class Product(models.Model):
    model = models.CharField('Название', max_length=20)
    description = models.TextField("Описание")
    image = models.ImageField(upload_to='media', verbose_name='Изображение')
    # image = models.FileField()

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
