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
    	zvphil = models.TextField(default='')
    	zpnumber = models.TextField(default='')
    	zemerg = models.TextField(default='')
    	hhrelat = models.TextField(default='')
    	zfccategories = models.TextField(default='')
    	hhrelat = models.TextField(default='')
    	rmgender= models.TextField(default='')
    	zbirth = models.TextField(default='')
    	municipality = models.ForeignKey(Municipality, default=None, on_delete=models.PROTECT)
    	class meta:
    		db_table ="mmPersonal_Info"
class Employment(models.Model):
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
    	vr1stdosedate = models.DateField(default='')
    	vr2nddosedate = models.DateField(default='')
    	vftestingcenter = models.TextField(default='')
    	vaccinator = models.TextField(default='')
    	personal_info = models.ForeignKey(Personal_Info, default=None, on_delete=models.PROTECT)
    	class meta:
     		db_table ="vvVaccination_Details"

class Comorbidities(models.Model):
    	cccomorbidity = models.TextField(default='')
    	callergies = models.TextField(default='')
    	diagnosedu = models.TextField(default='')
    	dicovid = models.TextField(default='')
    	datecovid = models.DateField(default='')
    	classcovid = models.TextField(default='')
    	personal_info = models.OneToOneField(Personal_Info, default=None, on_delete=models.PROTECT)
    	class meta:
    		db_table ="hhComorbidities"

  
  




# Create your models here.
   
  
  





# Create your models here.
