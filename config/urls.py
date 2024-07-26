"""
Конфигурация URL-адреса для проекта конфигурации.

Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Примеры:
Представления функций
    1. Добавьте импорт: из представлений импорта my_app.
    2. Добавьте URL-адрес в urlpatterns: path('',views.home, name='home')
Представления на основе классов
    1. Добавляем импорт: fromother_app.views import Home
    2. Добавьте URL-адрес в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Импортируйте функцию include(): из django.urls import include, путь
    2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('blog/', include('blog.urls', namespace='blog')),
]
if settings.DEBUG:  # dz_20.1
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # dz_20.1
