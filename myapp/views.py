from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, response
from .forms import EmpForm, StudentForm, UploadFileForm
from myapp.functions import handle_uploaded_file
from myapp.models import Employee
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from django.views.decorators.http import require_http_methods
from django.template import loader
def hello(request):
    template=loader.get_template('index.html')
    if request.method=='POST':
        form=StudentForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse('File uploaded succesfully')

    form=StudentForm()
    name={
        'student':'Arnab',
        'form':form
    }
    

    return HttpResponse(template.render(name, request))


@require_http_methods(["GET"])
def show(request):
     return HttpResponse("<h2> This is Http get Request</h2>")



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('Upload suncess fully')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})



def methodinfo(request):  
    return HttpResponse("Http request is: "+request.method)  


def getdata(request):  
    try:  
        data = Employee.objects.get(id=12)  
    except ObjectDoesNotExist:  
        return HttpResponse("Exception: Data not found")  
    return HttpResponse(data);  


import csv  
  
def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response 


from reportlab.pdfgen import canvas 



def getpdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment; filename="file.pdf'
    p=canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
   
    p.drawString(100,700, "Hello Arnab Podder")
    p.showPage()
    p.save()
    return response