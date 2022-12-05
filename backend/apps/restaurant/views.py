from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class RestaurantPage(TemplateView):
    template_name = "restaurant.html"