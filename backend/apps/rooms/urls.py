from django.urls import path
from backend.apps.rooms.views import *

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('about/',AboutPage.as_view(),name="about"),
    path('rooms_booking1/<int:booking_id>/',RoomsBookingPage.as_view(),name="rooms_booking"),
    path('booking_page/<int:booking_pk>/<int:room_pk>/',EndBookingView.as_view(),name="booking"),
    path('rooms/',RoomsPage.as_view(),name='rooms'),
    path('room_details/<int:pk>/',RoomDetail.as_view(),name='room_detail'),
    path('success/',SuccessView.as_view(),name='success'),
    path('spa_center/',SpaView.as_view(),name="spa_center")
]
