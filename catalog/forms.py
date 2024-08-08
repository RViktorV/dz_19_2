# 22.1 - Формы в Django вместо fields

from django import forms
from .models import Product, Version

PROHIBITED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'view_count', 'created_at', 'updated_at']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in PROHIBITED_WORDS:
            if word in name.lower():
                raise forms.ValidationError(f"Название продукта не должно содержать запрещенное слово: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in PROHIBITED_WORDS:
            if word in description.lower():
                raise forms.ValidationError(f"Описание продукта не должно содержать запрещенное слово: {word}") # от тут работает?
        return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_current']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control", })
        self.fields["is_current"].widget.attrs["class"] = "form-check-input"

    def clean_is_current(self):
        # cleaned_data = super().clean() # Это чее? )))
        cleaned_data = self.cleaned_data.get('is_current')
        # is_current = cleaned_data.get('is_current')
        product = self.instance.product if self.instance else None

        if cleaned_data and product:
            if Version.objects.filter(product=product, is_current=True).exclude(id=self.instance.id).exists():
                print("В райзе у вот же работает все, больше одного ставишь, принтует. Но исключения нет")
                raise forms.ValidationError('Для каждого продукта может быть только одна активная версия.')

        # Получаем текущие версии конкретного продута.
        # И если среди них есть ТЕКУЩИЕ, вызываем исключение
        # current_versions = Version.objects.filter(product=self.cleaned_data["product"], is_current=True)
        # if cleaned_data and current_versions:
        #     raise forms.ValidationError(
        #         f"Текущая версия может быть только одна. На данный момент установлена текущей: версия {current_versions[0]}")

        return cleaned_data


