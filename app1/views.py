from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=="POST":
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:

            return HttpResponse('data is not valid')
    return render(request,'insert_student.html',d)

