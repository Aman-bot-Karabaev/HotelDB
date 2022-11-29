from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm

from backend.apps.accounts.models import User, Comment



class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        widget= forms.TextInput(
            attrs = {"class":"login__input","placeholder":"Login"}
        )
    )
    password =forms.CharField(
        label = "Пароль",
        widget = forms.PasswordInput(
            attrs = {"class":"login__input","placeholder":"Password"}
        )
    )


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label = "Пароль",
        widget = forms.PasswordInput(
            attrs = {"class":"login__input","placeholder":"Password"}
        )
    )
    password2 = forms.CharField(
        label = "Повторите пароль:",
        widget = forms.PasswordInput(
            attrs = {"class":"login__input","placeholder":"Repeat password"}
        )   
    )


    class Meta:
        model = User
        fields = [
            "avatar",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone"
        ]
        form_control = {"class":"login__input"}
        widgets = {
            "avatar": forms.FileInput(attrs={"class":"login__input","placeholder":"Avatar"}),
            "username":forms.TextInput(attrs={"class":"login__input","type":"text", "placeholder":"Login"}),
            "first_name":forms.TextInput(attrs={"class":"login__input","type":"text", "placeholder":"Name"}),
            "last_name":forms.TextInput(attrs={"class":"login__input","type":"text", "placeholder":"Surname"}),
            "email": forms.EmailInput(attrs={"class":"login__input","type":"email", "placeholder":"Email"}),
            "phone": forms.TextInput(attrs={"class":"login__input","type":"text", "placeholder":"Phone"}),
        }

    
class UserPasswordChangeForm(SetPasswordForm):
    
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]



# class GuestInfiForm(forms.ModelForm):

#     class Meta:
#         model = Guest
#         fields = ["full_name","email"]
#         widgets = {
#             "full_name":forms.TextInput(attrs={"class":"profile__label","type":"text"}),
#             "email":forms.TextInput(attrs={"class":"profile__label","type":"text"})
#         }





class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content":forms.TextInput(
                attrs={"class":"profile__input profile__area","placeholder":"Your Comment*"}
            )
        }

