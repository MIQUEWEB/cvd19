from django.contrib import admin
from .models import Municipality, Personal_Info, Categories, Vaccination_Details, Comorbidities

admin.site.register(Municipality)
admin.site.register(Personal_Info)
admin.site.register(Categories)
admin.site.register(Vaccination_Details)
admin.site.register(Comorbidities)
# Register your models here.
