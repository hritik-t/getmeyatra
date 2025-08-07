"""
URL configuration for JourneyQuest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls.static import static
from .views import *
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='login'),
    path('signUp/', SignUp, name='signup'),
    path('bookdetails/', bookdetails, name='bookdetails'),
    # path('homePage/', homePage, name='homePage'),
    path('book/', book, name='book'),
    path('aboutUs/', aboutUs, name='aboutUs'),
    path('gallery/', gallery, name='gallery'),
    path('service/', service, name='service'),
    path('package/', package, name='package'),
    path('khatushyamdetail/', khatushyam, name='khatushyam'),
    path('dodhamdetail/', dodham, name='dodham'),
    path('ekdhamdetail/', ekdham, name='ekdham'),
    path('chardhamdetail/', chardham, name='chardham',),
    path('vrindavandetail/', vrindavan, name='vrindavan'),
    path('ujjaindetail/', ujjain, name='ujjain'),
    path('book-trip/', views.book_trip, name='book_trip'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('payment-response/', views.payment_response, name='payment_response'),
]
