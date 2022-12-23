from django.urls import path
from backend.apps.accounts.views import (
    LoginView, UserRegisterView, UserInfo, CreateCommentView,logout_user, ManagerView,restaurant_manager,InvalidUser,
    delete_booking, delete_rest_booking
    )



urlpatterns = [
    path('login/', LoginView.as_view(), name="sign_in"), 
    path('registration/', UserRegisterView.as_view(), name="register"),
    path("logout/", logout_user, name = "logout"),
    path('profile/<int:pk>',UserInfo.as_view(),name='profile'),
    path("create/comment/", CreateCommentView.as_view(), name="create_comment"), 
    path('manager/', ManagerView.as_view(), name='manager'),
    path('restaurant_manager',restaurant_manager,name='restaurant_manager'),
    path('invalid_user/',InvalidUser.as_view(),name='invalid'),
    path("booking/delete/<int:booking_id>/", delete_booking, name="delete_booking"),
    path("r_booking/delete/<int:booking_id>/", delete_rest_booking, name = "delete_rest_booking")
   
]