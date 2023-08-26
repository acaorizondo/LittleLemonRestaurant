from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.name}, {self.no_of_guests}, {self.booking_date}" 
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.SmallIntegerField()
    
    def __str__(self) -> str:
        return f"{self.title}, {self.price}, {self.inventory}" 