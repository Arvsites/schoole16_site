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

def n7(request):
    return render(request,'main/n7.html')

def n8(request):
    return render(request,'main/n8.html')

def n9(request):
    return render(request,'main/n9.html')

def n10(request):
    return render(request,'main/n10.html')

def n11(request):
    return render(request,'main/n11.html')

def n12(request):
    return render(request,'main/n12.html')

def n13(request):
    return render(request,'main/n13.html')

def n14(request):
    return render(request,'main/n14.html')

def n15(request):
    return render(request,'main/n15.html')

def n16(request):
    return render(request,'main/n16.html')

def n17(request):
    return render(request,'main/n17.html')

def n18(request):
    return render(request,'main/n18.html')

def n19(request):
    return render(request,'main/n19.html')

def n20(request):
    return render(request,'main/n20.html')