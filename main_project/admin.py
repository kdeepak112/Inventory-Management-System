from django.contrib import admin
from .models import product,location,ProductMovement
# Register your models here.

admin.site.register([product,location,ProductMovement])