from rest_framework import serializers
from .models import Flight,Passenger,Reservation


class Flightserializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class Passengerserializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class Reservationserializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

