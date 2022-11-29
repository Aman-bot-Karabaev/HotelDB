from django import forms


from backend.apps.rooms.models import Booking,Contact

        


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in','check_out','adult','children']
        widgets = {
        'check_in': forms.DateInput(
            format='%d-%m-%Y',
            attrs={'type': 'date', 'class': 'home__form-input'}),
        'check_out': forms.DateInput(
            format='%d-%m-%Y',
             attrs={'type': 'date', 'class': 'home__form-input'}
        ),
        "adult": forms.NumberInput(attrs={"class":"home__form-input"}),
        "children": forms.NumberInput(attrs={"class": "home__form-input"})
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message','phone' ]
        widgets = {
            'name': forms.TextInput(attrs={"class":"login__input","type":"text", "placeholder":"Name"}),
            'email': forms.EmailInput(attrs={"class":"login__input","type":"text", "placeholder":"Email"}),
            'message': forms.Textarea(attrs={"class":"login__input","type":"text", "placeholder":"Comment"}),
            'phone': forms.TextInput(attrs={"class":"login__input","type":"text", "placeholder":"Enter your phone number..."})
        }

