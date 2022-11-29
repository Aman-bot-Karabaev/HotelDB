from rest_framework import serializers
from backend.apps.rooms.models import Booking


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Booking
        fields = (
            'id', 'customer',
        )

class BookingSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bookings = serializers.SerializerMethodField()


    class Meta:
        model = Booking
        fields = (
            'check_in', 'check_out', 'room', 'sum'
        )