from django.contrib import admin

# Register your models here.

# podemos registrar el modelo aqui para que apresca en localhost/admin
from .models import Tasks
admin.site.register(Tasks)
