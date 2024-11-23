from django import forms
from  .models import *

class registerform(forms.ModelForm):
    class Meta:
        model=registerdata
        fields=['firstname','lastname','email','password','mobile','dob','city','gender','address','aadhar','familytype','image']

class registerupdateform(forms.ModelForm):
    class Meta:
        model=registerdata
        fields=['firstname','lastname','email','mobile','dob','city','gender','address','aadhar','familytype']

class passform(forms.ModelForm):
    class Meta:
        model=registerdata
        fields=['password']