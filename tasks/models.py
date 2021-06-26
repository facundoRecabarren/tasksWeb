from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# cada clase es una tabla de la BBDD

class Tasks(models.Model):
    
    # cada atributo es un nuevo campo de la tabla

    #esto ya que estado tiene 3 valores posibles
    class States(models.TextChoices):
        POR_COMENZAR = 'PC', _('por_comenzar')
        EN_PROCESO = 'EP', _('en_proceso')
        FINALIZADA = 'FN', _('finalizada')

    title = models.CharField(max_length=45)
    subtitle = models.CharField(max_length=45)
    limit_date = models.DateField()
    description = models.TextField()
    state = models.CharField(
        max_length=2,
        choices=States.choices,
        default=States.POR_COMENZAR,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)