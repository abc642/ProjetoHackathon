from django.db import models

class Element(models.Model):
    element = models.CharField(max_length=15,blank=True,null=True)
    symbol = models.CharField(max_length=3,blank=True,null=True)
    atomicNumber = models.IntegerField(blank=True,null=True)
    atomicMass = models.FloatField(blank=True,null=True)
    neutrons = models.IntegerField(blank=True,null=True)
    protons = models.IntegerField(blank=True,null=True)
    electrons = models.IntegerField(blank=True,null=True)
    phase = models.CharField(max_length=35,null=True,blank=True)
    radioactive = models.CharField(max_length=10,null=True,blank=True)
    tp = models.CharField(max_length=35,blank=True,null=True)

    def __str__(self):
        return self.element


