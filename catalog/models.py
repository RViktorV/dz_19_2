from django.db import models

from users.models import Users

# dz_20.1 все модели созданы в дз 20.1 до 34 строки

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование категории',
                            help_text='Введите наименование категории')
    description = models.TextField(verbose_name='Описание категории', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=225, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта', **NULLABLE)
    picture = models.ImageField(upload_to='product/photo', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория',
                                 **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    owner = models.ForeignKey(Users, verbose_name='Собственник товара', **NULLABLE, on_delete=models.SET_NULL)

    is_published = models.BooleanField(default=False, verbose_name="Опубликован")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price']
        permissions = [
            ("can_is_published_product", "Можно отменить публикацию продукта"),
            ("can_description_product", "Можно менять описание любого продукта"),
            ("can_category_product", "Можно изменить категорию продукта"),
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=50)
    version_name = models.CharField(max_length=255)
    is_current = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ['product']

    def __str__(self):
        return f" {self.version_name} ({self.version_number})"
