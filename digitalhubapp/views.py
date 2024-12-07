from django.shortcuts import render, redirect, get_object_or_404


from django.contrib import messages
from .forms import ContactForm
from django.template.context_processors import request

from .models import Service, Booking, Contact
from .forms import BookingForm

def home(request):
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

def payment(request):
    return render(request, 'payment.html')

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

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request,'terms.html')

def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')