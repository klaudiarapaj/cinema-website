from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ContactForm(forms.ModelForm):
        class Meta:
            model = Contact
            fields = ["firstname", "lastname", "phonenumber","email", "subject"]

class ReservationForm(forms.ModelForm):
        class Meta:
            model = Reservation
            fields = ['name', 'email', 'phone',"no_persons","movie"]      



    
   