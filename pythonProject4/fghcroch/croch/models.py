from django.db import models
from django.urls import reverse


class Products(models.Model):
    name = models.CharField('Название', max_length=100)
    content = models.TextField('Описание', blank=True, null=True)
    structure = models.CharField('Состав', blank=True, null=True, max_length=100)
    thickness = models.FloatField('Толщина инструмента', blank=True, null=True)
    tr_length = models.FloatField('Длина нити', blank=True, null=True)
    material = models.CharField('Материал', blank=True, null=True, max_length=100)
    size = models.FloatField('Размер', blank=True, null=True)
    color = models.CharField('Цвет', blank=True, null=True, max_length=100)
    photo = models.ImageField('Фото', blank=True)
    price = models.FloatField('Цена', max_length=10, null=True)
    cat = models.ForeignKey('Category', verbose_name="Категория", on_delete=models.PROTECT)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField('Категория', max_length=50)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
