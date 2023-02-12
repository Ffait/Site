from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import *

class AddProdForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Products
        fields = ['name', 'content', 'structure', 'thickness', 'tr_length', 'material', 'size', 'color', 'photo', 'price', 'cat', 'slug']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control text-bg-success'}),
                   'content': forms.Textarea(attrs={'class': 'form-control text-bg-success'}),
                   'structure': forms.TextInput(attrs={'class': 'form-control text-bg-success'}),
                   'thickness': forms.NumberInput(attrs={'class': 'form-control text-bg-success'}),
                   'tr_length': forms.NumberInput(attrs={'class': 'form-control text-bg-success'}),
                   'material': forms.TextInput(attrs={'class': 'form-control text-bg-success'}),
                   'size': forms.NumberInput(attrs={'class': 'form-control text-bg-success'}),
                   'color': forms.TextInput(attrs={'class': 'form-control text-bg-success'}),
                   'photo': forms.FileInput(attrs={'class': 'form-control form-control-sm text-bg-success'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control text-bg-success'}),
                   'cat': forms.Select(attrs={'class': 'form-control text-bg-success'}),
                   'slug': forms.TextInput(attrs={'class': 'form-control text-bg-success'})
                   }

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control text-bg-success'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control text-bg-success'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control text-bg-success'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control text-bg-success'}))
    first_name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'form-control text-bg-success'}))
    last_name = forms.CharField(label='Фамилия', required=False, widget=forms.TextInput(attrs={'class': 'form-control text-bg-success'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control text-bg-success'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control text-bg-success'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control text-bg-success'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control text-bg-success'}))
    content = forms.CharField(label='Напишите текст', widget = forms.Textarea(attrs={'class': 'form-control text-bg-success', 'cols': 50, 'rows': 4}))
    captcha = CaptchaField(label='Введите текст с картинки')