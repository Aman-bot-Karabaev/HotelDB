from django.urls import path
from backend.apps.accounts.views import (
    LoginView, UserRegisterView, UserInfo, CreateCommentView,logout_user,insert,manager
)



urlpatterns = [
    path('login/', LoginView.as_view(), name="sign_in"), 
    path('registration/', UserRegisterView.as_view(), name="register"),
    path("logout/", logout_user, name = "logout"),
    path('profile/<int:pk>',UserInfo.as_view(),name='profile'),
    path("create/comment/", CreateCommentView.as_view(), name="create_comment"), 
    path('manager/', manager, name='manager'),
    path('manager/insert', insert, name='insert' )
   
]