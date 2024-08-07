from django.core.checks import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['object_list']

        active_versions = {}
        for product in products:
            current_versions = product.versions.filter(is_current=True)
            if current_versions.count() == 1:
                active_versions[product.id] = current_versions.first()
            elif current_versions.count() > 1:
                messages.error(self.request,
                               f"Product {product.name} Имеет несколько активных версий. Убедитесь, что установлена только одна активная версия..")

        context['active_versions'] = active_versions
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object

        active_version = product.versions.filter(is_current=True).first()
        if active_version:
            context['active_version'] = active_version

        return context



# 22.1 - Формы в Django вместо fields
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_form.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_form.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_confirm_delete.html'


class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        # Обработка GET запроса
        return render(request, self.template_name)

    def post(self, request):
        # Обработка POST запроса
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя-{name}, Телефон-{phone}, Сообщение-{message}")
        return render(request, self.template_name)
