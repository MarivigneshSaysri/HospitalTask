from django.db import models
from App2.models import receptionist
from datetime import timezone






class hospital(models.Model):
    Name = models.CharField(default="",max_length=20)
    Address_line1 = models.CharField(default="",max_length=100)
    Address_line2 = models.CharField(default="",max_length=100)
    District = models.CharField(default="",max_length=100)
    State = models.CharField(default="",max_length=100)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)






    def __str__(self):
        return self.Name


class doctor(models.Model):
        
        Name = models.CharField(default="",max_length=20)
        Gender = models.CharField(default="",max_length=10)
        Specialist = models.CharField(default="",max_length=40)
        isActive = models.BooleanField(default=True,help_text="0-Inactive,1-active")
        created_by = models.ForeignKey(receptionist,on_delete=models.SET_NULL,null=True,related_name="Doctors_created")
        updated_by = models.ForeignKey(receptionist,on_delete=models.SET_NULL,null=True,related_name="Doctors_updated")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)


        def __str__(self):
            return self.Name

class patient(models.Model):

    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE)
    Name = models.CharField(default="",max_length=20)
    Age = models.CharField(default="",max_length=20)
    Initial_Disease = models.CharField(default="",max_length=50)
    created_by = models.ForeignKey(receptionist,on_delete=models.SET_NULL,null=True,related_name="Patients_created")
    updated_by = models.ForeignKey(receptionist,on_delete=models.SET_NULL,null=True,related_name="patients_updated")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 


    def __str__(self):
        return self.Name


class Slot(models.Model):
     slot1 = models.DateTimeField()
     duration =  models.CharField(choices=[("AM","AM"),("PM","PM")],default="AM",max_length=2)

     def __str__(self):
          return f"{self.slot1}{self.duration}"
    



class Schedule(models.Model):
     doctor_id = models.ForeignKey(doctor,on_delete=models.CASCADE)
     slot_id = models.ForeignKey(Slot,on_delete=models.CASCADE)
     patient_id = models.ForeignKey(patient,on_delete=models.CASCADE)
     created_by = models.ForeignKey(receptionist,on_delete=models.CASCADE,null=True,related_name="slot_created") 
     updated_by = models.ForeignKey(receptionist,on_delete=models.CASCADE,null=True,related_name="slot_updated") 
     created_at = models.DateTimeField(null=True,auto_now_add=True)
     updated_at = models.DateTimeField(null=True,auto_now=True)

     def __str__(self):
          return f"Doctor Id is {self.doctor_id.Name},Patient Id is {self.patient_id.Name},TIME{self.slot_id}"

    






# Create your models here.
