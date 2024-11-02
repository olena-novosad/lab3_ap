from django.db import models

# Create your models here.
class Aeroport(models.Model):
    name_of_aeroport = models.CharField(max_length=100)
    code_of_aeroport = models.CharField(max_length=10)
    location = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.name_of_aeroport} ({self.code_of_aeroport})"

class Gate(models.Model):
    number_of_gate = models.CharField(max_length=20)
    status_of_gate = models.CharField(max_length=40)
    aeroport = models.ForeignKey(Aeroport, on_delete=models.CASCADE, related_name='gates')

    def __str__(self):
        return f"Gate {self.number_of_gate} - {self.status_of_gate}"

class Flight(models.Model):
    flight_number = models.CharField(max_length=45)
    time_of_departure = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airline = models.CharField(max_length=100)
    aeroport = models.ForeignKey(Aeroport, on_delete=models.CASCADE, related_name='flights')
    boarding_time = models.DateTimeField()
    destination = models.CharField(max_length=250)
    gate = models.ForeignKey(Gate, on_delete=models.CASCADE, related_name='flights')

    def __str__(self):
        return f"{self.flight_number} to {self.destination}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=30, unique=True)
    nationality = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Ticket(models.Model):
    ticket_number = models.CharField(max_length=25, unique=True)
    price = models.IntegerField()
    seat_number = models.CharField(max_length=10)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tickets')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return f"Ticket {self.ticket_number} - Seat {self.seat_number}"
