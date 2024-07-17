from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Smartphones(models.Model):
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField(
        validators = [MinValueValidator(100), MaxValueValidator(2000)]
    )
    especificacion = models.CharField(null=True, max_length=100)
    posee_camara = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.modelo} - {self.precio}"