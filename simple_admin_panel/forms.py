from django import forms
from django.forms import ModelForm
from .models import BlogPost



class RegistrationForm(forms.Form):
    username = forms.CharField(label="Логин", max_length=100)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    email = forms.EmailField(max_length=50)
    first_name = forms.CharField(label="Имя", max_length=30)
    last_name = forms.CharField(label="Фамилия", max_length=50)


class PostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text',]