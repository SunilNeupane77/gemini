from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.
def home(request):
    if request.method=='GET':
        form = UserForm()
    return render(request,'home.html',{'form':form})

def aboutus(request):
    return  render(request,"aboutus.html") 

def dynamicHome(request,id):
    print(id)
    return HttpResponse(f"<h1>dynamic Home Page {id}</h1>")

def sunil(request):
    return render(request,'sunil.html')

def division(request):
    return render(request,"division.html")