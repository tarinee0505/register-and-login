from django.shortcuts import render
from django.http import HttpResponse
from app.models import * 
# Create your views here.

def register(request):
    if request.method =="POST":
        name = request.POST.get('nme')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        cpw = request.POST.get('cpw')
        if pw==cpw:
            CO = Details(name=name, pno=pno, email=email, un=un, pw=pw)
            CO.save()
            return render(request,'login.html')
    return render(request,'register.html')


def login(request):
    if request.method =="POST":
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        UO = Details.objects.all()
        for user in UO:
            if user.un==un:
                if user.pw==pw:
                    return HttpResponse('logged in successfully')
                return HttpResponse('invalid password')
        else:
            return HttpResponse('user not found')
    return render(request,'login.html')
