from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_date = models.DateField()
    guests = models.PositiveIntegerField(max_length=6)

    def __str__(self):
        return f"{self.name} - {self.booking_date} - {self.guests} guests"

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(max_length=5)
    
    def __str__(self):
        return f"{self.title} - ${self.price} - {self.inventory} in stock"