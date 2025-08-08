from django.db import models

# Create your models here.

class Book(models.Model):
    Place=models.CharField(max_length=100)
    Total_person= models.CharField(max_length=2)
    Adate=models.CharField(max_length=10)
    Ldate=models.CharField(max_length=10)
    Personaldata=models.TextField()


class TripBooking(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    date = models.DateField()
    pickup_point = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    alt_phone = models.CharField(max_length=10, blank=True, null=True)
    persons = models.PositiveIntegerField()
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default="Pending")  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.date} - {self.to_location}"
    

