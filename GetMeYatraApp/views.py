from django.shortcuts import render, HttpResponse, redirect,  get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from .models import Book, TripBooking
from datetime import datetime
from django.conf import settings
import base64
from Crypto.Cipher import AES

# Create your views here.

def home(request):
    return render(request, 'homepage.html')


# def homePage(request):
#     return render(request, 'homepage.html')

def bookdetails(request):
    return render(request, 'bookingdetails.html')

def khatushyam(request):
    return render(request, 'khatushyamdetail.html')

def dodham(request):
    return render(request, 'dodhamdetail.html')

def ekdham(request):
    return render(request, 'ekdhamdetail.html')

def chardham(request):
    return render(request, 'chardhamdetail.html')

def vrindavan(request):
    return render(request, 'vrindavandetail.html')

def ujjain(request):
    return render(request, 'ujjaindetail.html')





def book_trip(request):
    if request.method == 'POST':
        from_location = request.POST.get('from')
        to_location = request.POST.get('to')
        date_str = request.POST.get('date')  
        pickup_point = request.POST.get('pickup')
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        alt_phone = request.POST.get('altPhone')
        persons = int(request.POST.get('persons'))
        price_per_person = float(request.POST.get('price'))
        total_price = persons * price_per_person

        # Convert date from DD-MM-YYYY to a Python date object
        if date_str:
            try:
                date = datetime.strptime(date_str, "%d-%m-%Y").date()
            except ValueError:
                return render(request, 'bookingdetials.html', {
                    'error': 'Invalid date format. Please select a valid date.'
                })
        else:
            return render(request, 'bookingdetials.html', {
                'error': 'Please select a date.'
            })

        # Save booking
        booking = TripBooking.objects.create(
            from_location=from_location,
            to_location=to_location,
            date=date,
            pickup_point=pickup_point,
            full_name=full_name,
            email=email,
            phone=phone,
            alt_phone=alt_phone,
            persons=persons,
            price_per_person=price_per_person,
            total_price=total_price
        )

        # Prepare CCAvenue payment
        merchant_id = settings.CCAV_MERCHANT_ID
        access_code = settings.CCAV_ACCESS_CODE
        working_key = settings.CCAV_WORKING_KEY
        redirect_url = request.build_absolute_uri('/payment-response/')

        data = f"merchant_id={merchant_id}&order_id={booking.id}&currency=INR&amount={total_price}&redirect_url={redirect_url}&billing_name={full_name}&billing_email={email}"

        cipher = AES.new(working_key.encode('utf-8'), AES.MODE_ECB)
        block_size = 16
        pad = block_size - len(data) % block_size
        data_padded = data + pad * chr(pad)  # PKCS5 padding
        encrypted = base64.b64encode(cipher.encrypt(data_padded.encode('utf-8'))).decode('utf-8')

        return render(request, 'ccavenue_redirect.html', {'encRequest': encrypted, 'access_code': access_code})

    # GET request
    return render(request, 'bookingdetials.html')



def payment_response(request):
    if request.method == 'POST':
        enc_response = request.POST.get('encResp')
        working_key = settings.CCAV_WORKING_KEY

        # Decrypt response
        cipher = AES.new(working_key.encode('utf-8'), AES.MODE_ECB)
        decrypted = cipher.decrypt(base64.b64decode(enc_response)).decode('utf-8').rstrip("\x00")

        # Convert decrypted string to dict
        response_data = dict(item.split('=') for item in decrypted.split('&'))
        order_id = response_data.get('order_id')
        status = response_data.get('order_status')  # Success / Failure / Aborted

        # Update booking
        booking = get_object_or_404(TripBooking, id=order_id)
        booking.payment_status = status
        booking.save()

        return render(request, 'payment_result.html', {'status': status, 'booking': booking})




def booking_success(request):
    return render(request, 'booking_success.html')


def book(request):
    if request.method=='POST':
        place = request.POST.get('place')
        total_person = request.POST.get('person')
        adate = request.POST.get('Adate')
        ldate = request.POST.get('Ldate')
        personaldata = request.POST.get('text')

        if place != '' and len(total_person) != 0 and adate != '' and ldate != 0 and personaldata != '':
            data = Book(Place=place, Total_person=total_person,
                             Adate=adate,Ldate=ldate,
                             Personaldata =personaldata)
            
            data.save()
    return render(request, 'book.html')


def package(request):
    return render(request, 'package.html')


def service(request):
    return render(request, 'service.html')


def gallery(request):
    return render(request, 'gallery.html')


def aboutUs(request):
    return render(request, 'about.html')


def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password in incorrect!!")
    return render(request, 'login.html')
 
def SignUp(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm are not same!! ")
        
        else:
            my_user=User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')