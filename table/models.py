from django.db import models

class Element(models.Model):
    element = models.CharField(max_length=15,blank=True,null=True)
    symbol = models.CharField(max_length=3,blank=True,null=True)
    atomicNumber = models.IntegerField(blank=True,default=0)
    atomicMass = models.FloatField(blank=True,default=0)
    neutrons = models.IntegerField(blank=True,default=0)
    protons = models.IntegerField(blank=True,default=0)
    electrons = models.IntegerField(blank=True,default=0)
    phase = models.CharField(max_length=35,null=True,blank=True)
    radioactive = models.CharField(max_length=10,null=True,blank=True)
    tp = models.CharField(max_length=35,blank=True,null=True)

    def __str__(self):
        return self.element




class Comercio(models.Model):
    tipo = models.CharField(max_length=15)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField(max_length=240)
    cidade = models.CharField(max_length=30)
    numero = models.IntegerField()
    imagem = models.CharField(max_length=240)

    def __str__(self):
        return self.titulo
