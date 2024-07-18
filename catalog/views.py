from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    item_name = Product.objects.all()
    context = {
        'items': item_name
    }
    return render(request, 'catalog/product_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print((f"Имя-{name},Телефон-{phone},Сообщение-{message}"))
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    # Получение объекта товара по его первичному ключу
    product = get_object_or_404(Product, pk=pk)

    # Формирование контекста для шаблона
    context = {
        'item': product
    }

    # Рендеринг шаблона с переданным контекстом
    return render(request, 'catalog/product_detail.html', context)

