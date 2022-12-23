# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from backend.apps.restaurant.models import RestaurantBook
# from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render,redirect
from django.views.generic import FormView, CreateView, DetailView, ListView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
# from django.views.generic.edit import FormMixin
from rest_framework import viewsets


# Create your views here.


from backend.apps.accounts.models import User
# from backend.apps.rooms.models import Rooms
from backend.apps.accounts.forms import LoginForm, UserRegisterForm, CommentForm
from backend.apps.rooms.views import Contact
from backend.apps.rooms.models import Booking
from backend.apps.rooms.forms import StatusForm
# from .serializers import BookingSerializer

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data["username"]
        password = data["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                if not user.is_authenticated:
                    return HttpResponseRedirect(reverse('register'))
                elif user.groups.filter(name='manager').exists():
                    return redirect('manager')
                else: 
                    login(self.request, user)
                    return redirect("index")
            return HttpResponse("<h1>You account is not active</h1")
        return redirect('invalid')



def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("sign_in")




class UserRegisterView(CreateView):
    template_name =  "signUp.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("sign_in")

class ProfilePage(FormView):
    template_name = 'profile.html'
    form_class = CommentForm


class UserInfo(LoginRequiredMixin, DetailView):
    template_name = 'profile.html'
    model = User
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context    

class CreateCommentView(LoginRequiredMixin, FormView):
    form_class = CommentForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)




 
# Create your views here.
class ManagerView(FormView):
    form_class = StatusForm
    template_name = 'manager_page.html'
    model = Booking
    success_url = reverse_lazy('manager')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_bookings'] = Booking.objects.all()
        return context


    def form_valid(self, form):
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
     
        return super().form_valid(form)



def restaurant_manager(request):
    all_restaurant_bookings = RestaurantBook.objects.all()
    return render(request, 'restaurant_manager.html', {'all_restaurant_bookings': all_restaurant_bookings})
 
class InvalidUser(TemplateView):
    template_name = "invalid_user.html"



def change_booking_status(request, booking_pk):
    pass


def delete_booking(request, booking_id):
    Booking.objects.get(id=booking_id).delete()
    return redirect(reverse_lazy('manager'))

def delete_rest_booking(request, booking_id):
    RestaurantBook.objects.get(id=booking_id).delete()
    return redirect(reverse_lazy('restaurant_manager'))