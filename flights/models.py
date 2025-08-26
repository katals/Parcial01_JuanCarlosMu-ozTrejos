from django.db import models

# Create your models here.
class Flight(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    FLIGHT_TYPE_CHOICES = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]

    # Creamos el campo 'flight_type' y le asignamos las opciones.
    flight_type = models.CharField(
        default='Nacional',
        max_length=15,
        choices=FLIGHT_TYPE_CHOICES,
        verbose_name="Tipo de Vuelo"
    )

    def __str__(self):
        return f"{self.name} - {self.price}"

