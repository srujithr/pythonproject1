from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class customusers(AbstractUser):
    Title = models.CharField(max_length=244)
    address = models.CharField(max_length=225, null=True)
    user_type = models.CharField(max_length=255,null=True)
    image = models.FileField()
    phone = models.IntegerField(null=True)
    location = models.CharField(max_length=255,null=True)
    company_name = models.CharField(max_length=225,null=True)

    def __str__(self):
        return self.username



class Car(models.Model):
    company_id = models.ForeignKey(customusers, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    image = models.FileField()
    car_model = models.CharField(max_length=225,null=True)
    details = models.TextField(max_length=255,null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(customusers, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    no_of_days = models.IntegerField(null=True)
    day = models.DateTimeField(auto_now_add=True)
    Total_cost = models.IntegerField(null=True)
    booking_date = models.DateField(default=timezone.now)
    status = models.CharField(default='pending',max_length=255)
    review = models.CharField(max_length=255,null=True)
    Rating = models.IntegerField(null=True)




