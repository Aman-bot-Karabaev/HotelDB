from django.urls import path
from backend.apps.accounts.views import (
    LoginView, UserRegisterView, UserInfo, CreateCommentView, BookingViewSet,logout_user
)



# from django.conf.urls import  include
# from rest_framework import routers
# from backend.apps.accounts import views


# router = routers.DefaultRouter()
# router.register(r'accounts', views.BookingViewSet)


# urlpatterns = [
#     path('^api/', include(router.urls)),
#     path('', views.index, name='accounts')
# ]



urlpatterns = [
    path('login/', LoginView.as_view(), name="sign_in"), 
    path('registration/', UserRegisterView.as_view(), name="register"),
    path("logout/", logout_user, name = "logout"),
    path('profile/<int:pk>',UserInfo.as_view(),name='profile'),
    path("create/comment/", CreateCommentView.as_view(), name="create_comment"), 
    path('manager/', BookingViewSet.as_view({'get':'list'}), name='manager')
   
]