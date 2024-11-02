from rest_framework import serializers
from .models import Aeroport, Gate, Flight, Passenger, Ticket

class AeroportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeroport
        fields = '__all__'

class GateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'