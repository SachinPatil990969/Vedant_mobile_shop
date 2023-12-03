# Q 4) What is Django URLs?make program to create django urls

# In Django, URLs are defined in the urls.py file. This file contains the URL patterns for the application, mapping URLs to views. Here's a simple example:

# In app's urls.py file
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Add more URL patterns as needed
]
