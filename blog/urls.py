# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.country_list, name='country_list'),  # List of countries
    path('countries/<str:name>/', views.country_detail, name='country_detail'),  # Country details
]
