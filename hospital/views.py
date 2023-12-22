from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect
from .models import Doctor,Patient
# Create your views here.
def About(request):
    return render(request,'about.html')
def Home(request):
    return render(request, 'home.html')
def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password = p)
        try:
            if user.is_staff:
                login(request,user)
                error = 'no'
            else:
                error ="yes"
        except:
            error ="yes"
    d = {'error':error}
    return render(request, 'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    logout(request)
    return redirect('admin_login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)
def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id = pid)
    doctor.delete()
    return redirect('view_doctor')
@csrf_protect
def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['Name']
        m = request.POST['mobile']
        sp = request.POST['special']
        img = request.FILES['image']
        try:
            Doctor.objects.create(Name=n,mobile=m,special=sp,image = img)
            error = 'no'
        except:
            error ="yes"
    d = {'error':error}
    return render(request, 'add_doctor.html',d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d={'doc':doc}
    return render(request,'view_patient.html',d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id = pid)
    patient.delete()
    return redirect('view_patient')

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        pn = request.POST['name']
        m = request.POST['mobile']
        g = request.POST['gender']
        a = request.POST['address']
        try:
            Patient.objects.create(name=pn,mobile=m,gender=g,address = a)
            error = 'no'
        except:
            error ="yes"
    d = {'error':error}
    return render(request, 'add_patient.html',d)