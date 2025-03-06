from django.urls import path 
from .import views 

urlpatterns = [
    path("",views.scheduletab,name="scheduletab"),
    path("doctors",views.doctors,name = "doctors"),
    path("patients",views.patients,name="patients"),
    path("receptionist",views.receiptionist,name="receptionist")
   
]