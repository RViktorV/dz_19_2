from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import modelformset_factory

from catalog.forms import ProductForm, VersionForm
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
            if current_versions.count() == 1:
                active_versions[product.id] = current_versions.first()
            elif current_versions.count() > 1:
                messages.error(self.request,
                               f"Product {product.name} имеет несколько активных версий. Убедитесь, что установлена только одна активная версия.")

        context['active_versions'] = active_versions
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object

        current_versions = product.versions.filter(is_current=True)
        if current_versions.count() == 1:
            context['active_version'] = current_versions.first()
        elif current_versions.count() > 1:
            messages.error(self.request,
                           f"Product {product.name} имеет несколько активных версий. Убедитесь, что установлена только одна активная версия.")

        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version_form'] = VersionForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        version_form = VersionForm(request.POST)
        if form.is_valid() and version_form.is_valid():
            product = form.save()
            version = version_form.save(commit=False)
            version.product = product
            version.save()
            return redirect(self.success_url)
        return self.form_invalid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        version = Version.objects.filter(product=self.object).first()
        context['version_form'] = VersionForm(instance=version)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        version = Version.objects.filter(product=self.object).first()
        version_form = VersionForm(request.POST, instance=version)
        if form.is_valid() and version_form.is_valid():
            product = form.save()
            version = version_form.save(commit=False)
            version.product = product
            version.save()
            return redirect(self.success_url)
        return self.form_invalid(form)


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


ProductForm.version_form = VersionForm()

# from django.core.checks import messages
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views import View
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#
# from catalog.forms import ProductForm
# from catalog.models import Product
#
#
# class HomeListView(ListView):
#     model = Product
#     template_name = 'home.html'
#     context_object_name = 'object_list'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         products = context['object_list']
#
#         active_versions = {}
#         for product in products:
#             current_versions = product.versions.filter(is_current=True)
#             if current_versions.count() == 1:
#                 active_versions[product.id] = current_versions.first()
#             elif current_versions.count() > 1:
#                 messages.error(self.request,
#                                f"Product {product.name} Имеет несколько активных версий. Убедитесь, что установлена только одна активная версия..")
#
#         context['active_versions'] = active_versions
#         return context
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'catalog/product_detail.html'
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product = self.object
#         current_versions = product.versions.filter(is_current=True)
#         if current_versions.count() == 1:
#             context['active_version'] = current_versions.first()
#         elif current_versions.count() > 1:
#             messages.error(self.request,
#                            f"Product {product.name} имеет несколько активных версий. Убедитесь, что установлена только одна активная версия.")
#
#         return context
#         active_version = product.versions.filter(is_current=True).first()
#         if active_version:
#             context['active_version'] = active_version
#
#         return context
# #
#
#
# # 22.1 - Формы в Django вместо fields
# # class ProductCreateView(CreateView):
# #     model = Product
# #     form_class = ProductForm
# #     success_url = reverse_lazy('catalog:home')
# #     template_name = 'catalog/product_form.html'
#
#
# class ProductCreateView(CreateView):
#     model = Product
#     form_class = ProductForm
#     success_url = reverse_lazy('catalog:home')
#     template_name = 'catalog/product_form.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['version_form'] = VersionForm()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         version_form = VersionForm(request.POST)
#         if form.is_valid() and version_form.is_valid():
#             product = form.save()
#             version = version_form.save(commit=False)
#             version.product = product
#             version.save()
#             return redirect(self.success_url)
#         return self.form_invalid(form)
#
# class ProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductForm
#     success_url = reverse_lazy('catalog:home')
#     template_name = 'catalog/product_form.html'
#
#
# class ProductDeleteView(DeleteView):
#     model = Product
#     success_url = reverse_lazy('catalog:home')
#     template_name = 'catalog/product_confirm_delete.html'
#
#
# class ContactsView(View):
#     template_name = 'catalog/contacts.html'
#
#     def get(self, request):
#         # Обработка GET запроса
#         return render(request, self.template_name)
#
#     def post(self, request):
#         # Обработка POST запроса
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"Имя-{name}, Телефон-{phone}, Сообщение-{message}")
#         return render(request, self.template_name)
