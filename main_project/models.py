from django.db import models

# Create your models here.
from django.db import models
import datetime

# Create your models here.


class product(models.Model):

    product_id = models.AutoField
    product_name = models.CharField(max_length=5)

    def __str__(self):
        return 'Product:'+self.product_name


class location(models.Model):

    location_id = models.AutoField
    location = models.CharField(max_length=2)

    def __str__(self):
        return 'Location ID:'+self.location


class ProductMovement(models.Model):

    movement_id = models.AutoField
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    from_location = models.ForeignKey(
        location, related_name='+', on_delete=models.CASCADE,null=True,blank=True)
    to_location = models.ForeignKey(
        location, related_name='+', on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(
        product, related_name='+', on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return 'ProductMovement:'+self.product_id.product_name
