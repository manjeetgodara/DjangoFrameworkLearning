from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     persons=[
          {'name':"Manjeet",'age':23},
          {'name':"Pankaj",'age':24},
           {'name':"Vicky",'age':13},
          {'name':"Sunny",'age':24},
           {'name':"Rajesh",'age':17},
          {'name':"Vikas",'age':34},
     ]
     return render(request,'index.html',context={'people':persons})

def service(request):
   return render(request,'service.html')
