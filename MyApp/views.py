from django.shortcuts import render,redirect
from MyApp.models import Emp
from . import forms
# Create your views here.
def EmpView(request):
    emp_list=Emp.objects.all()
    my_dict={'elist':emp_list}
    return render(request,'MyApp/MyPage.html',context=my_dict)

def EmpReg(request):
    form=forms.EmpForm()
    my_dict={'form':form}
    return render(request,'MyApp/Register.html',context=my_dict)
    return redirect('home')

def home(request):
    return render(request,'MyApp/home.html', {}) 

def login_user(request):
    
    return render(request,'MyApp/login.html', {}) 
    return redirect('home')

def Myinfo(request):
    return render(request, 'MyApp/Myinfo.html', {})          
