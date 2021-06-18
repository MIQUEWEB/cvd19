from django.db import models


class Municipality(models.Model):
    	ukmunicipality = models.TextField(default='')
    	yybaranggay = models.TextField(default='')
        xxregion = models.TextField(default='')  			
    	class meta:
    		db_table ="rrmunicipality"
class Personal_Info(models.Model):
    	zflname = models.TextField(default='')
    	znaddress = models.TextField(default='')
        rremail = models.TextField(default='')
    	zpngender = models.TextField(default='')
    	zpnumber = models.TextField(default='')
    	zvphilhealth = models.TextField(default='')
        emergencyy = models.TextField(default='')
        hhrelationship = models.TextField(default='')
    	zrmbirthday= models.TextField(default='')
        zfccategories = models.TextField(default='')
    	municipality = models.ForeignKey(Municipality, default=None, on_delete=models.PROTECT)
    	class meta:
    		db_table ="mmPersonal_Info"
class Employement(models.Model):
    	zfcemployed = models.TextField(default='')
        employnst = models.TextField(default='')
        occu = models.TextField(default='')
        employern = models.TextField(default='')
        eaddr = models.TextField(default='')
    	personal_info = models.ForeignKey(Personal_Info, default=None, on_delete=models.PROTECT)
    	class meta:
    		db_table ="mmemploeyee"

class Vaccination_Details(models.Model):
    	vpbrandname = models.TextField(default='')
    	vr1stdose2nd= models.TextField(default='')
    	vadategiven= models.DateTimeField(default='')
    	vftestingcenter = models.TextField(default='')
        vaccintor = models.TextField(default='')
    	personal_info = models.ForeignKey(Personal_Info, default=None, on_delete=models.PROTECT)
    	class meta:
     		db_table ="vvVaccination_Details"

class Comorbidities(models.Model):
    	cccomorbidity = models.TextField(default='')
    	callergies = models.TextField(default='')
        diagnosedu = models.TextField(default='')
    	personal_info = models.OneToOneField(Personal_Info, default=None, on_delete=models.PROTECT)
    	class meta:
    		db_table ="hhComorbidities"
    
  
  




# Create your models here.
   
  
  





# Create your models here.
