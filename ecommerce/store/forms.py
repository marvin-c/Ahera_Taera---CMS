from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    dob = forms.DateField(localize=True, widget=forms.DateInput(format = '%d-%m-%Y',attrs={'type': 'date'}),)
    phonenumber = forms.CharField(max_length=20)
    street = forms.CharField(max_length=50)
    suburb = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    postcode = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'password1', 
                  'password2', 
                  'dob',
                  'phonenumber',
                  'street',
                  'suburb',
                  'city',
                  'country',
                  'postcode',
                  )