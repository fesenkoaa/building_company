from django import forms
from .models import EnNewEmployee
from building_business_card.models import Contact


class EnContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* name'}),
        label="", required=True
    )
    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* phone without "+"'}),
        label="", required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        label="", required=False
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* message'}),
        label="", required=True
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'phone', 'email', 'message')


class EnNewEmployeeForm(forms.ModelForm):

    class Meta:

        model = EnNewEmployee
        fields = ('position', 'first_name', 'last_name', 'phone', 'year', 'location')
        widgets = {
            'position': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone without "+"'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }