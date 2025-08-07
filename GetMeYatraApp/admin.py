from django.contrib import admin
from .models import TripBooking, Book


admin.site.register(Book)

class TripBookingAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'from_location',
        'to_location',
        'date',
        'pickup_point',
        'persons',
        'price_per_person',
        'total_price',
        'phone',
        'alt_phone',
        'email',
        'payment_status',
        'created_at',
    )
    list_filter = ('date', 'from_location', 'to_location', 'pickup_point', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'alt_phone','date','to_location')
    readonly_fields = ('created_at', 'total_price')  

    
    def save_model(self, request, obj, form, change):
        obj.total_price = obj.persons * obj.price_per_person
        super().save_model(request, obj, form, change)

# Register TripBooking with custom admin
admin.site.register(TripBooking, TripBookingAdmin)
