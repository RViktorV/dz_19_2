from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product


class HomeListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


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
