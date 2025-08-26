from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.FlightRegisterView, name='registerFlight'),
    path('list/', views.FlightsListView, name='flightsList'),
    path('stats/', views.FlightsStatsView, name='flightsStats'),
]