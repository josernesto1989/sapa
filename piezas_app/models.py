from django.db import models

# Create your models here.
class Modelo(models.Model):
    name = models.CharField(max_length=255)
    

class Marca(models.Model):
    name = models.CharField(max_length=255)

class TipoPieza(models.Model):
    name = models.CharField(max_length=255)
    
    
class Taller(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    