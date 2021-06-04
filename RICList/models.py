from django.db import models


class Municipality(models.Model):
    	ukmunicipality = models.TextField(default='')
    	yybaranggay = models.TextField(default='')			
    	class meta:
    		db_table ="rrmunicipality"
class Personal_Info(models.Model):
    	zflname = models.TextField(default='')
    	znaddress = models.TextField(default='')
    	zpngender = models.TextField(default='')
    	zpnumber = models.TextField(default='')
    	zvphilhealth = models.TextField(default='')
    	zrmbirthday= models.TextField(default='')
    	municipality = models.ForeignKey(Municipality, default=None, on_delete=models.PROTECT)
    	class meta:
    		db_table ="mmPersonal_Info"
class Categories(models.Model):
    	zfccategories = models.TextField(default='')
    	personal_info = models.ForeignKey(Personal_Info, default=None, on_delete=models.PROTECT)
    	class meta:
    		db_table ="ccCategories"

class Vaccination_Details(models.Model):
    	vpbrandname = models.TextField(default='')
    	vr1stdose2nd= models.TextField(default='')
    	vadategiven= models.DateTimeField(default='')
    	vftestingcenter = models.TextField(default='')
    	personal_info = models.ForeignKey(Personal_Info, default=None, on_delete=models.PROTECT)
    	class meta:
     		db_table ="vvVaccination_Details"

class Comorbidities(models.Model):
    	cccomorbidity = models.TextField(default='')
    	callergies = models.TextField(default='')
    	personal_info = models.OneToOneField(Personal_Info, default=None, on_delete=models.PROTECT)
    	class meta:
    		db_table ="hhComorbidities"
    
  
  




# Create your models here.
   
  
  





# Create your models here.
