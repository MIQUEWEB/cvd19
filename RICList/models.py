
from django.db import models


class COVIDList(models.Model):
    pass


class Item(models.Model):
    zflname = models.TextField(default='')
    znaddress = models.TextField(default='')
    zpnumber = models.TextField(default='')
    zrmbirthday= models.TextField(default='')
    zvaccine = models.TextField(default='') 
    list = models.ForeignKey(COVIDList, default=None, on_delete=models.PROTECT)

  
  




# Create your models here.
