from config.settings import CACHE_ENABLED
from catalog.models import Category
from django.core.cache import cache

def get_category_from_cach():
    '''
    Получение категорий из кэша, если кэш включен, если не включен - из базы данных
    '''
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'catalog_list'
    catalog = cache.get(key)
    if catalog is not None:
        return catalog
    catalog = Category.objects.all()
    cache.set(key, catalog)
    return catalog

