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
        "adult": forms.NumberInput(attrs={"class":"home__form-input","placeholder":"Adult"}),
        "children": forms.NumberInput(attrs={"class": "home__form-input","placeholder":"Children"})
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message','phone' ]
        widgets = {
            'name': forms.TextInput(attrs={"class":"profile__input","type":"text", "placeholder":"Full Name"}),
            'email': forms.EmailInput(attrs={"class":"profile__input","type":"text", "placeholder":"Email"}),
            'message': forms.Textarea(attrs={"class":"profile__input profile__area","type":"text", "placeholder":"Message"}),
            'phone': forms.TextInput(attrs={"class":"profile__input","type":"text", "placeholder":"Phone number"})
        }


