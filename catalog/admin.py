from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "description",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("version_number", "version_name", 'is_current')
    search_fields = ("is_current", "version_name",)