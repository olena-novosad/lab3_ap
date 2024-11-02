from django.shortcuts import render
from rest_framework import viewsets
from .models import Aeroport, Gate, Flight, Passenger, Ticket
from .serializers import AeroportSerializer, GateSerializer, FlightSerializer, PassengerSerializer, TicketSerializer

class AeroportViewSet(viewsets.ModelViewSet):
    queryset = Aeroport.objects.all()
    serializer_class = AeroportSerializer

class GateViewSet(viewsets.ModelViewSet):
    queryset = Gate.objects.all()
    serializer_class = GateSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

