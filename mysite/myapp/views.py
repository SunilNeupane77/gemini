from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def aboutus(request):
    return  render(request,"aboutus.html") 

def dynamicHome(request,id):
    print(id)
    return HttpResponse(f"<h1>dynamic Home Page {id}</h1>")

def sunil(request):
    return render(request,'sunil.html')

def division(request):
    return render(request,"division.html")