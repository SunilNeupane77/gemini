from django.contrib import admin
from .models import Person
from .models import Vehicles

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
   list_display=["id","first_name"]
   
@admin.register(Vehicles)
 class vehiclesnaem(admin.ModelAdmin):
    list_display=["model_number","color"]