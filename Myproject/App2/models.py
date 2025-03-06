from django.db import models




class receptionist(models.Model):
    Name = models.CharField(default="",max_length=30)
    email = models.EmailField(default="",max_length=100,unique=True)
    password = models.CharField(default="",max_length=12)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by =models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Name
# Create your models here.
