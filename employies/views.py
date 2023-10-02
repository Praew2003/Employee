from django.shortcuts import render

from . import models
# Create your views here.

def home(request):
    context = {}
    information = models.Information.objects.all()
    context['informations'] = information
    
    return render(request,'index.html', context)

def purchasing(request):
    context = {}
    department = models.Department.objects.get(id=1)
    
    information = models.Information.objects.filter(department=department)
    context['informations'] = information
    
    return render(request,'purchasing.html', context)

def providing(request):
    context = {}
    department = models.Department.objects.get(id=2)
    
    information = models.Information.objects.filter(department=department)
    context['informations'] = information
    
    return render(request,'providing.html', context)

def aftersale(request):
    context = {}
    department = models.Department.objects.get(id=3)
    
    information = models.Information.objects.filter(department=department)
    context['informations'] = information
    
    return render(request,'aftersale.html', context)

def about (request):
    return render(request,"about.html")