from dal import autocomplete
from django import forms
# from suit.widgets import EnclosedInput

from stock.models import Linea


class LineaForm(forms.ModelForm):
    class Meta:
        model = Linea
        fields = '__all__'
        widgets = {
            'linea': autocomplete.ModelSelect2(url='linea-autocomplete'),
        }
