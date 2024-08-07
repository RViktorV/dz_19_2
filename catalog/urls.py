from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .views import ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]
