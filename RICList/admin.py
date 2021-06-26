from django.contrib import admin
from .models import Municipality, Personal_Info, Vaccination_Details, Comorbidities, Employment

admin.site.register(Municipality)
admin.site.register(Personal_Info)
admin.site.register(Employment)
admin.site.register(Vaccination_Details)
admin.site.register(Comorbidities)
# Register your models here.
