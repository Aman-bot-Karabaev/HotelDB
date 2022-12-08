from django import forms
from backend.apps.restaurant.models import RestaurantBook


class BookTable(forms.ModelForm):
    class Meta:
        model = RestaurantBook
        fields = [
            "name",
            "phone",
            "email",
            "time",
            "persons"
           
        ]
        form_control = {"class":"login__input"}
        widgets = {
            "name":forms.TextInput(attrs={"class":"login__input",'type':'text',"placeholder":"Full name"}),
            "phone":forms.TextInput(attrs={"class":"login__input",'type':'tel',"placeholder":"Phone"}),
            "email":forms.EmailInput(attrs={"class":"login__input",'type':'email',"placeholder":"Email"}),
            "time":forms.DateTimeInput(attrs={"class":"login__input","type":"datetime-local"}),
            "persons":forms.TextInput(attrs={"class":"login__input",'type':'text',"placeholder":"Persons"})
        }