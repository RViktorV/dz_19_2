
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('users/', include('users.urls', namespace='users')),
]
if settings.DEBUG:  # dz_20.1
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # dz_20.1
