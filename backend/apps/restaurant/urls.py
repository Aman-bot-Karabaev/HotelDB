from django.urls import path
from backend.apps.restaurant.views import *

urlpatterns = [
    path('restaurant/', RestaurantPage.as_view(), name="restaurant"),
    path('success/',SuccessView.as_view(),name='successs')]