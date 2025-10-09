from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    numero = forms.CharField(
        max_length=8,
        min_length=8,
        label="Número",
        widget=forms.TextInput(attrs={'placeholder': '12345678'})
    )

    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'direccion', 'numero']  # Omitimos 'telefono'

    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if not numero.isdigit():
            raise forms.ValidationError("Solo debe contener números.")
        return numero

    def save(self, commit=True):
        instance = super().save(commit=False)
        numero = self.cleaned_data['numero']
        instance.telefono = '+569' + numero
        if commit:
            instance.save()
        return instance