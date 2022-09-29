from django.db import models

# Create your models here.
class Moneda(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()

    def __str__(self):
        return self.name   

class Marca(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  

class Modelo(models.Model):
    name = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    def __str__(self):
        return self.name   
    

 

class TipoPieza(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name   

class Estado(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  

class Pieza(models.Model):    
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)#TODO: cambiar a muchos
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#manytomanyfield
    tipoPieza = models.ForeignKey(TipoPieza, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    price = models.FloatField()
    cost = models.FloatField()
    min_amount = models.FloatField()
    priority = models.IntegerField()

    def __str__(self):
        return self.marca.__str__()+"/"+self.modelo.__str__()+"/"+self.tipoPieza.__str__()   

class Location(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name   

class Taller(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)    
    def __str__(self):
        return self.name

class Inventario(models.Model):
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name   