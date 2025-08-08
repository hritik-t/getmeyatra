from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Sum
from .models import TripBooking
from collections import defaultdict

class TripBookingAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone',
        'pickup_point',
        'to_location',
        'persons',
        'created_at',
        'date',
        'price_per_person',
        'total_price',
        'alt_phone',
        'email',
        'payment_status',
    )
    list_filter = ('to_location', 'date', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'alt_phone', 'date', 'to_location')
    readonly_fields = ('created_at', 'total_price')

    def save_model(self, request, obj, form, change):
        obj.total_price = obj.persons * obj.price_per_person
        super().save_model(request, obj, form, change)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'date-wise-bookings/',
                self.admin_site.admin_view(self.date_wise_view),
                name='date-wise-bookings',
            ),
            path(
                'location-date-summary/',
                self.admin_site.admin_view(self.location_date_summary_view),
                name='location-date-summary',
            ),
        ]
        return custom_urls + urls

    def date_wise_view(self, request):
        TOTAL_SEATS = 52

        bookings = (
            TripBooking.objects
            .values('date', 'to_location')
            .annotate(total_booked=Sum('persons'))
            .order_by('date')
        )

        for booking in bookings:
            booking['remaining'] = TOTAL_SEATS - booking['total_booked']

        context = dict(
            self.admin_site.each_context(request),
            bookings=bookings,
            title='Date-wise Trip Booking Summary',
        )
        return TemplateResponse(request, "admin/date_wise_bookings.html", context)

    def location_date_summary_view(self, request):
        records = TripBooking.objects.values_list('to_location', 'date').order_by('to_location', 'date')

        grouped = defaultdict(set)  # use set to avoid duplicates
        for to_location, date in records:
            grouped[to_location].add(date)  # sets automatically remove duplicates

        # Sort dates after converting from set to list
        summary = [
            {'to_location': loc, 'dates': sorted(dates)} 
            for loc, dates in grouped.items()
        ]

        context = dict(
            self.admin_site.each_context(request),
            summary=summary,
            title='Destinations and Dates Summary',
        )
        return TemplateResponse(request, "admin/location_date_summary.html", context)


admin.site.register(TripBooking, TripBookingAdmin)
