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
    nome = forms.CharField(max_length=30)
    sobrenome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)



    class Meta:
        model = User
        fields = ('username','nome','sobrenome',
                  'email','password1','password2',)


