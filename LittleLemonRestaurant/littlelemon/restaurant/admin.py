from django.contrib import admin
from .models import Booking, Menu

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Price', 'Inventory')
@admin.register(Booking)    
class BookingAdmin(admin.ModelAdmin):
    list_display=('Name','No_of_guests','Booking_Date')