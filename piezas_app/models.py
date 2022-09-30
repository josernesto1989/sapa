from django.db import models

# Create your models here.
class Moneda(models.Model):
    name = models.CharField(max_length=255, unique=True)
    value = models.FloatField()

    def __str__(self):
        return self.name   

class Marca(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name  

class Modelo(models.Model):
    name = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    def __str__(self):
        return self.name   
    

 

class TipoPieza(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name   

class Estado(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name  
#*********************** ManyToMany Examples
# class Publication(models.Model):
#     title = models.CharField(max_length=30)

#     class Meta:
#         ordering = ['title']

#     def __str__(self):
#         return self.title

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)

#     class Meta:
#         ordering = ['headline']

#     def __str__(self):
#         return self.headline

class Pieza(models.Model):    
    modelo = models.ManyToManyField(Modelo)#TODO: cambiar a muchos
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#manytomanyfield
    tipoPieza = models.ForeignKey(TipoPieza, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    price = models.FloatField()
    cost = models.FloatField()
    min_amount = models.FloatField()
    priority = models.IntegerField()

    def __str__(self):
        modelos= ""
        for s in self.modelo.all():
            modelos +=s.__str__()+";"
        return self.tipoPieza.__str__()+"/"+modelos[:-1]   

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