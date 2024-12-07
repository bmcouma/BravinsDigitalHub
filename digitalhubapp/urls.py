from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('payment/', views.payment, name='payment'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('service-details/<int:service_id>/', views.service_details, name='service-details'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('booking/', views.booking, name='booking'),
    path('manage-bookings/', views.manage_bookings, name='manage_bookings'),
    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit-booking'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete-booking'),
    path('service-details/<slug:slug>/', views.service_details, name='service_details'),
    path('services/', views.services, name='services'),
    path('terms/', views.services, name='terms'),
    path('privacy/', views.services, name='privacy'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),

]