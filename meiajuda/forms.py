from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Person
from django.forms import ModelForm



class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['titulo','categoria','descricao','imagem','numero','cidade',
                  'cep',]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,help_text='Nome')
    last_name = forms.CharField(max_length=100,help_text='Sobrenome')
    email = forms.EmailField(max_length=200,help_text='Email')



    class Meta:
        model = User
        fields = ('username','first_name','last_name',
                  'email','password1','password2',)


