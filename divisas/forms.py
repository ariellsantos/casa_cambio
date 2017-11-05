from django import forms

from .models.monedero import Monedero
from .models.moneda import Moneda

class MonederoForm(forms.ModelForm):
    moneda = forms.ModelChoiceField(queryset=Moneda.objects.all())

    class Meta:
        model = Monedero
        fields = ('nombre',)
    
    def __init__(self, *args, **kwargs):
        super(MonederoForm, self).__init__(*args, **kwargs)
        self.fields['moneda'].widget.attrs.update({'class' : 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
        