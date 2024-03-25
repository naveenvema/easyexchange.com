from .models import *
from django import forms
from django.forms import ModelForm


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20, required=True)
    city=forms.CharField(max_length=70,required=True)
    class Meta:
        model=User
        fields=['username','email','city','password1','password2','phone_number']

class ProductsForm(ModelForm):
    class Meta:
        model=Sellerproducts
        fields="__all__"
        exclude=['status','customer']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }