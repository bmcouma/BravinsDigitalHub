from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from django.template.context_processors import request
from .models import Service, Booking, Contact, Member, TeamMember, ImageModel
from .forms import BookingForm,  ImageUploadForm

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')  # Capture phone number from the user
        amount = request.POST.get('amount')  # Amount to be paid

        # Safaricom API credentials
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'
        business_shortcode = 'your_shortcode'
        passkey = 'your_passkey'

        # Generate access token
        auth_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        response = requests.get(auth_url, auth=(consumer_key, consumer_secret))
        access_token = response.json().get('access_token')

        # STK Push request
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {'Authorization': f'Bearer {access_token}'}
        payload = {
            "BusinessShortCode": business_shortcode,
            "Password": passkey,  # Generate password dynamically
            "Timestamp": "your_timestamp",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": business_shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": "your_callback_url",
            "AccountReference": "YourService",
            "TransactionDesc": "Payment for services"
        }

        response = requests.post(api_url, json=payload, headers=headers)
        return JsonResponse(response.json())
    return JsonResponse({"error": "Invalid request"}, status=400)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def booking(request):
    if request.method == 'POST':
       mybooking=Booking(

           name=request.POST['name'],
           email=request.POST['email'],
           phone=request.POST['phone'],
           service=request.POST['service'],
           amount=request.POST['amount'],
           status=request.POST['status'],
           mpesa_number=request.POST['mpesa_number'],
           notes=request.POST['notes'],

       )
       mybooking.save()
       return redirect('/booking')  # Properly aligned with the `if` block
    else:
        return render(request, 'booking.html')

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')

def faqs(request):
    return render(request, 'faqs.html')

def manage_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'manage-bookings.html', {'bookings': bookings})

def pricing(request):
    return render(request, 'pricing.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def service_details(request):
    return render(request, 'service-details.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def team(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully.")
            return redirect('manage_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking.html', {'form': form})


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, 'Booking deleted successfully!')
    return redirect('manage_bookings')


def services(request):
    services_list = Service.objects.all()
    return render(request, 'services.html', {'services': services_list})

def terms(request):
    return render(request,'terms.html')

def register(request):
   if request.method == 'POST':
       members = Member(
           name=request.POST['name'],
           username=request.POST['username'],
           password=request.POST['password']
       )
       members.save()
       return redirect('/login')
   else:
       return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            member = Member.objects.get(username=username)
            if check_password(password, member.password):
                return render(request, 'index.html', {'member': member})
            else:
                messages.error(request, 'Invalid password.')
        except Member.DoesNotExist:
            messages.error(request, 'User does not exist.')
        return redirect('login')
    return render(request, 'login.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')