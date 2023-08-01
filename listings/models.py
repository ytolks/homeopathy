from django.db import models
from datetime import datetime

# Create your models here.
class Listing(models.Model):
    homeopathy_name = models.CharField(max_length=200)
    potency_30 = models.BooleanField(null=True)
    potency_200 = models.BooleanField(null=True)
    potency_1m = models.BooleanField(null=True)
    potency_ml1 = models.BooleanField(null=True)
    quantity_of_30 = models.IntegerField(null=True)
    quantity_of_200= models.IntegerField(null=True)
    quantity_of_1m = models.IntegerField(null=True)
    quantity_of_ml1 = models.IntegerField(null=True)
    description = models.TextField(null=True,max_length=400,blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True,null=True)

    def __str__(self):
         return self.homeopathy_name

