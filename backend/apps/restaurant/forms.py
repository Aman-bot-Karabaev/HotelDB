from django import forms
from backend.apps.restaurant.models import RestaurantMenu

class MenuForm(forms.ModelForm):

    class Meta:
        model = RestaurantMenu
        fields = [
            "name",
            "category",
            "price",
            "info",
        ]
        widgets = {
            "name":forms.CharField(attrs={"class":"menu__list-title"})
        }
