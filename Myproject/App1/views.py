from django.shortcuts import render
from .models import * 
from App2.models import receptionist
from .forms import receptionisttable,patienttable

def receiptionist(request):
    formtable = receptionisttable()
    return render(request,'receptionist.html',{"formtable":formtable})

def scheduletab(request):
    schedule = Schedule.objects.all() 
    forms = patienttable()
    return render(request,'index.html',{"schedule":schedule,"forms":forms})


def doctors(request):
    alldoctors = doctor.objects.all()
    return render(request,'doctors.html',{"doctors":alldoctors})

def patients(request):
    patients = patient.objects.all()
    return render(request,'patients.html',{"patients":patients})