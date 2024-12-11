from django.db import models
from django.utils import timezone

# Model for team members
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='team_profiles/', blank=True, null=True)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Model for portfolio items
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    technologies_used = models.TextField()

    def __str__(self):
        return self.title

# Model for client testimonials
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.rating}"

# Model for clients
class Client(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Model for services
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Model for bookings
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=100, default="Unknown")
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    mpesa_number = models.CharField(max_length=15, blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Booking {self.id} by {self.name}"

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.subject}'

class Member(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title