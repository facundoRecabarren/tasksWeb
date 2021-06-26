from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from PIL import Image

# Create your models here.
class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField(default='14092.jpg',upload_to='profileImages')

    #sobrecargar la funcion save, para escalar el tamaño de la imagen
    def save(self):
        super().save()
        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            new_size = (300,300)
            image.thumbnail(new_size)
            image.save(self.image.path)