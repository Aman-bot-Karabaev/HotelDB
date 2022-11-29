from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView,ListView, CreateView
from django.views import View


from backend.apps.rooms.models import Rooms,Booking,Contact
from .forms import BookingForm,ContactForm
from backend.apps.accounts.models import Comment
# Create your views here.


class IndexPage(CreateView):
    template_name = 'index.html'
    form_class = BookingForm
    model = Booking 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Rooms.objects.all()
        context["comments"] = Comment.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        if self.request.user.is_authenticated:
            instance.user = self.request.user
        instance.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        booking_id = self.object.id
        print(booking_id)
        return reverse_lazy('rooms_booking', kwargs={"booking_id":booking_id})

    
class RoomsBookingPage(ListView):
    template_name = 'rooms_booking1.html'
    model = Rooms
    queryset = Rooms.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        booking_id = self.kwargs.get("booking_id")
        context["booking_pk"] = booking_id
        return context

from django.shortcuts import get_object_or_404

class EndBookingView(View):

    def get(self, request, booking_pk, room_pk):
        booking = get_object_or_404(Booking, pk=booking_pk)
        room = get_object_or_404(Rooms, pk=room_pk)
        booking.room = room
        booking.save()
        form = ContactForm()
        context = {
            "booking":booking,
            "form":form,
        }
        return render(request,"booking_page.html",context)
    

    def post(self, request):
        form = ContactForm(request.POST)
        contact = form.save()
        
        





class RoomsPage(ListView):
    template_name = 'rooms.html'
    model = Rooms
    queryset = Rooms.objects.all()




class AboutPage(TemplateView):
    template_name = 'about.html'
    