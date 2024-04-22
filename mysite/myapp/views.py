from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>This is Home Page<h1>")

def aboutus(request):
    return HttpResponse("<h1>This is about us page</h1>")

def dynamicHome(request,id):
    print(id)
    return HttpResponse(f"<h1>dynamic Home Page {id}</h1>")