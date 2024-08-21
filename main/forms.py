from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import Parking_Place


class CreateUserForm(UserCreationForm):
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']


class ReservedForm(forms.ModelForm):
    class Meta:
        model = Parking_Place
        fields = ['start', 'end']

    start = forms.DateTimeField(
        required=True,
        widget=forms.TextInput(attrs={'type':'datetime-local','class': 'form-control'}),
    )
    end = forms.DateTimeField(
        required=True,
        widget=forms.TextInput(attrs={'type':'datetime-local','class': 'form-control'}),
    )


class EnterForm(forms.ModelForm):
    class Meta:
        model = Parking_Place
        fields = ['place']

    place = forms.ModelChoiceField(
        queryset=Parking_Place.objects.filter(status=['PF', 'PR']),
        to_field_name='id',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class ExitForm(forms.ModelForm):
    class Meta:
        model = Parking_Place
        fields = ['place']

    place = forms.ModelChoiceField(
        queryset=Parking_Place.objects.filter(status='PT'),
        to_field_name='id',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
