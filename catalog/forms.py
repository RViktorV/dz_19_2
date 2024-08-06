# 22.1 - Формы в Django вместо fields

from django import forms
from .models import Product

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
                raise forms.ValidationError(f"Описание продукта не должно содержать запрещенное слово: {word}")
        return description
