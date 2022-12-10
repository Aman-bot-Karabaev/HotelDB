from django.shortcuts import render,redirect
from django.views.generic import FormView,TemplateView
from .forms import BookTable

# Create your views here.

class RestaurantPage(FormView):
    template_name = "restaurant.html"
    form_class = BookTable
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.save()
        return redirect('successs')

class SuccessView(TemplateView):
    template_name = 'successs.html'

