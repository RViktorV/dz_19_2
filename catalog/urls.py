from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    CategoryListView, CategoryDetailView
from .views import ContactsView

app_name = CatalogConfig.name


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('catalog/<int:pk>/delete/', cache_page(60)(ProductDeleteView.as_view()), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

]
