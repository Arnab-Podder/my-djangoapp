from cProfile import label
from django import forms

from .models import Student

class EmpForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"



class StudentForm(forms.Form):
    first_name=forms.CharField(label="Enter Your First Name", max_length=50)
    last_name=forms.CharField(label="Enter Your Last Name", max_length=100)
    file = forms.FileField() 


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()