from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView,ListView, CreateView
from django.views import View
from django.http import HttpResponse
from django.conf import settings
 
from backend.apps.rooms.models import Rooms,Booking,Contact
from .forms import BookingForm,ContactForm
from backend.apps.accounts.models import Comment,User
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
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError

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
    

    def post(self, request,booking_pk, room_pk):
        form = ContactForm(request.POST)
        contact = form.save()
        booking = get_object_or_404(Booking, pk=booking_pk)
        booking.customer = contact 
        booking.status = Booking.BOOKING_STATUS_NEW
        booking.save()
        if form.is_valid():
                email = form.cleaned_data["email"]
             
                subject = "success booking"
                email_template_name = "success_booking_email.html"
                message_data = {
                "email":email,
            }
                text_email = render_to_string(email_template_name, message_data)
                try:
                    r=send_mail(subject=subject,message=text_email,
                    recipient_list=[email],
                    from_email = settings.EMAIL_HOST_USER,
                    fail_silently=True,)
                    print(r)
                except BadHeaderError:
                    return HttpResponse("Invalid Header")
                return redirect(reverse_lazy("success"))
        
         
        return redirect("success")
        


class RoomsPage(ListView):
    template_name = 'rooms.html'
    model = Rooms
    queryset = Rooms.objects.all()
 
class RoomDetail(DetailView):
    template_name = "room_details.html"
    model = Rooms
    queryset = Rooms.objects.filter()
    

class AboutPage(TemplateView):
    template_name = 'about.html'

class SuccessView(TemplateView):
    template_name = "success.html"