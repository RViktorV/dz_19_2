# Создадим кастомный шаблонный тег для доступа к элементам словаря.
# Для этого добавим новый файл и зарегистрируем наш шаблонный тег.
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)