from django.shortcuts import render, redirect
from django import forms
from .models import Flight
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import models

# Create your views here.

def home(request):
    return render(request, 'home.html')

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        # Especifica los campos del modelo que quieres en el formulario
        fields = ['name', 'flight_type', 'price']

# 2. La vista debe ser una función (usando 'def'), no una clase.
def FlightRegisterView(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FlightForm()
        
    return render(request, 'registerFlight.html', {'form': form})

def FlightsListView(request):
    flights = Flight.objects.all()
    return render(request, 'flightsList.html', {'flights': flights})

def FlightsStatsView(request):
    total_flights = Flight.objects.count()
    avg_price = Flight.objects.all().aggregate(models.Avg('price'))['price__avg'] or 0
    return render(request, 'flightsStats.html', {
        'total_flights': total_flights,
        'avg_price': avg_price
    })
