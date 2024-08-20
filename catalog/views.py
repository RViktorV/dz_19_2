from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory, forms, BaseInlineFormSet

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version


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
            active_versions[product.id] = current_versions.first()

        context['active_versions'] = active_versions
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_form.html'

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_form.html'

    def get_context_data(self, **kwargs):
        """
        Расширьте данные контекста с помощью набора форм для управления связанными экземплярами «Версии».

        Этот метод создает встроенный набор форм для модели «Версия», связанной с «Продуктом».
        пример. Набор форм включается в контекстные данные, которые передаются в шаблон.
        для рендеринга.

        Если метод запроса — POST, он привязывает набор форм к данным POST для обработки формы.
        подчинение. В противном случае он инициализирует набор форм существующими экземплярами «Версия».
        связанный с текущим объектом `Product`.

        Аргументы:
            **kwargs: в метод передаются дополнительные контекстные данные.

        Возврат:
            dict: обновленные данные контекста, включая набор форм для управления экземплярами «Версия».
        """

        context_data = super().get_context_data(**kwargs)                                           # Получить существующие данные контекста из родительского класса
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)     # Создайте встроенную фабрику наборов форм для модели «Версия», связанной с моделью «Продукт».
        if self.request.method == 'POST':                                                       # Проверьте, является ли метод запроса POST (отправка формы)
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)   # Если POST, привяжите набор форм к данным POST.
        else:
            context_data['formset'] = VersionFormset(instance=self.object)                      # Если не POST, инициализируйте набор форм существующими экземплярами Version.
        return context_data                                                                     # Вернуть обновленные данные контекста

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data.get('formset')
        if formset.is_valid():
            active_versions_count = sum(1 for form in formset if form.cleaned_data.get('is_current'))
            if active_versions_count > 1:
                formset.non_form_errors = ['Вы можете выбрать только одну активную версию для продукта.']
                return self.form_invalid(form)  # Возвращаем ошибку формы
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perms([
            "catalog.can_is_published_product",
            "catalog.can_description_product",
            "catalog.can_category_product",
        ]):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_confirm_delete.html'


class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя-{name}, Телефон-{phone}, Сообщение-{message}")
        return render(request, self.template_name)
