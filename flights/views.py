from django.shortcuts import render, redirect
from django import forms
from .models import Flight
from django.db.models import Avg

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
    national_flights_count = Flight.objects.filter(flight_type='Nacional').count()
    international_flights_count = Flight.objects.filter(flight_type='Internacional').count()
    national_avg_price = Flight.objects.filter(flight_type='Nacional').aggregate(Avg('price'))['price__avg'] or 0
    context = {
        'national_flights_count': national_flights_count,
        'international_flights_count': international_flights_count,
        'national_flights_avg_price': national_avg_price,
    }

    return render(request, 'flightsStats.html', context)
