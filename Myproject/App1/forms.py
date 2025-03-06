from django import forms 
from App2.models import receptionist 
from .models import *  


class receptionisttable(forms.ModelForm):
    class Meta:
        model = receptionist
        fields = "__all__"

class patienttable(forms.ModelForm):
    class Meta:
        model = patient
        fields= "__all__"