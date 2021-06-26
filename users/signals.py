from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Usuarios

#cuando un usuario es creado se manda esta "señal" que será recibida por el @receiver
#el receiver ejecuta esta funcion

#al crear un usuario creamos un perfil(acá llamado Usuarios)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Usuarios.objects.create(user=instance)

#kwarg acepta parametros adicionales 
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.usuarios.save()