from django.db import models

# Create your models here.

class TourPackage(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='tour_images/')
    description = models.TextField()  # Short description (homepage)
    full_description = models.TextField()  # Overview paragraph
    duration = models.CharField(max_length=50)
    meals = models.CharField(max_length=100)
    transportation = models.CharField(max_length=100)
    pickup_points = models.CharField(max_length=200)
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)

    # Optional: For tabs content
    itinerary = models.TextField()
    inclusions = models.TextField()
    exclusions = models.TextField()
    important_note = models.TextField()
    hotel_details = models.TextField()

    def __str__(self):
        return self.name




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
    

