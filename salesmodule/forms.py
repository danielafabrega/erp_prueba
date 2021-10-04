from django import forms

from .models import Booksale

class BookSaleForm(forms.ModelForm):

    class Meta:
        model = Booksale
        fields = ('product', 'month_year', 'document_number', 'iva')