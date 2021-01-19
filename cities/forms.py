from django import forms

from cities.models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Miasto',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Wprowadź nazwę Miasta'
                           }))

    class Meta:
        model = City
        fields = ('name', )
