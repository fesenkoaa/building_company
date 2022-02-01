from django import forms
from .models import Contact, NewEmployee, Vacancy


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* имя'}),
        label="", required=True
    )
    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* телефон без "+"'}),
        label="", required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        label="", required=False
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* сообщение'}),
        label="", required=True
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'phone', 'email', 'message')


class NewEmployeeForm(forms.ModelForm):

    class Meta:

        model = NewEmployee
        fields = ('position', 'first_name', 'last_name', 'phone', 'year', 'location')
        widgets = {
            'position': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'номер без "+"'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }