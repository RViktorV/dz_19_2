import os
import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Load data from JSON file into the database, clearing existing data first.'

    def handle(self, *args, **kwargs):
        # Загрузка данных из JSON-файла
        with open('catalog/catalog_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Удаление всех продуктов
        Product.objects.all().delete()
        self.stdout.write(self.style.WARNING('All products have been deleted.'))

        # Удаление всех категорий
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING('All categories have been deleted.'))

        # Создание категорий
        categories_data = [item for item in data if item['model'] == 'catalog.category']
        categories_for_create = []
        for item in categories_data:
            fields = item['fields']
            category = Category(
                id=item['pk'],
                name=fields['name'],
                description=fields['description'],
            )
            categories_for_create.append(category)

        Category.objects.bulk_create(categories_for_create)
        self.stdout.write(self.style.SUCCESS('Categories have been created.'))

        # Создание продуктов
        products_data = [item for item in data if item['model'] == 'catalog.product']
        products_for_create = []
        for item in products_data:
            fields = item['fields']
            product = Product(
                id=item['pk'],
                name=fields['name'],
                description=fields.get('description', ''),
                image=fields.get('image', ''),
                category=Category.objects.get(pk=fields['category']),
                price=fields['price'],
                created_at=fields['created_at'],
                updated_at=fields['updated_at']
            )
            products_for_create.append(product)

        Product.objects.bulk_create(products_for_create)
        self.stdout.write(self.style.SUCCESS('Products have been created.'))

        self.stdout.write(self.style.SUCCESS('Data has been successfully loaded into the database.'))
