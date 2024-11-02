from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Aeroport, Gate, Flight, Passenger, Ticket

@admin.register(Aeroport)
class AeroportAdmin(admin.ModelAdmin):
    list_display = ('name_of_aeroport', 'code_of_aeroport', 'location')

@admin.register(Gate)
class GateAdmin(admin.ModelAdmin):
    list_display = ('number_of_gate', 'status_of_gate', 'aeroport')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'destination', 'airline', 'time_of_departure')

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'passport_number', 'nationality')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'flight', 'passenger', 'seat_number', 'price')
