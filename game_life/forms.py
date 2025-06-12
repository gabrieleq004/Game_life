from django import forms
from .models import Recensione

class RecensioneForm(forms.ModelForm):
    class Meta:
        model = Recensione
        fields = ['gioco', 'cliente', 'contenuto', 'voto']
        widgets = {
            'contenuto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'voto': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
            'gioco': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'gioco': 'Gioco',
            'cliente': 'Utente',
            'contenuto': 'Recensione',
            'voto': 'Voto (1-10)'
        }
