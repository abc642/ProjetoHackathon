from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Person(models.Model):
    titulo = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='clients_photos',null=True,blank=True)
    numero = models.IntegerField()
    cep = models.IntegerField()
    cidade = models.CharField(max_length=30)


    def __str__(self):
        return self.titulo

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=150,verbose_name="Seu email aqui")
    begin_date = models.DateTimeField(auto_now_add=True)
    '''era False'''
    signup_confirmation = models.BooleanField(default=False)
    '''atributos do anuncio'''

    def __str__(self):
        return self.user.username



@receiver(post_save,sender=User)
def update_profile_signal(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()







    