from django.shortcuts import render
from  .models import Task, Country


def index(request):
    tasks = Task.objects.all()
    return render(request,'main/index.html', {'title':'Главная страница сайта', 'tasks':tasks})

def n1(request):
    return render(request,'main/n1.html' )

def n2(request):
    return render(request,'main/n2.html')

def n3(request):
    return render(request,'main/n3.html')

def n4(request):
    return render(request,'main/n4.html')

def n5(request):
    return render(request,'main/n5.html')

def n6(request):
    return render(request,'main/n6.html')