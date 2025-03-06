from django.contrib import admin
from .models import doctor,hospital,patient,Slot,Schedule

admin.site.register(doctor)
admin.site.register(hospital)
admin.site.register(patient)
admin.site.register(Slot)
admin.site.register(Schedule)


# Register your models here.
