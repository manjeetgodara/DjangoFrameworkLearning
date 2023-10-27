from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required






# Create your views here.
@login_required(login_url="/login/")
def recipe(request):
        if request.method=="POST":
             data=request.POST

             recipe_name=data.get("recipe_name")
             recipe_desc=data.get("recipe_desc")
             recipe_img=request.FILES.get("recipe_img")
             Recipe.objects.create(recipe_name=recipe_name,recipe_desc=recipe_desc,recipe_img=recipe_img)
            
             
             return redirect("/add_recipe")
        

        queryset=Recipe.objects.all()
        

        if request.GET.get('search'):
              print(request.GET.get('search'))
              queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))

        context={"recipe_data":queryset}       



        return render(request,'recipe.html',context)

def delete_recipe(request,id):
       queryset=Recipe.objects.get(id=id)
       queryset.delete()
       print(id)

       return redirect("/add_recipe")

def update_recipe(request,id):
       queryset=Recipe.objects.get(id=id)
       context={"recipe":queryset}
       if request.method=="POST":
             data=request.POST

             recipe_name=data.get("recipe_name")
             recipe_desc=data.get("recipe_desc")
             recipe_img=request.FILES.get("recipe_img")
             
             queryset.recipe_name=recipe_name
             queryset.recipe_desc=recipe_desc
             if recipe_img:
               queryset.recipe_img=recipe_img

             queryset.save()  

             return redirect("/add_recipe")
             
       
       
       return render(request,'update.html',context)


def register(request):
      if request.method=="POST":
           first_name=request.POST.get('first_name')
           last_name=request.POST.get('last_name')
           username=request.POST.get('username')
           password=request.POST.get('password')
           if  User.objects.filter(username=username).exists():
                messages.error(request,"Username is already taken")
               
           else:
                 user=User.objects.create(
                 first_name=first_name,
                 last_name=last_name,
                 username=username
                )
                 user.set_password(password)
                 user.save()
                
                    

           return redirect("/login/")

      
      return render(request,'register.html')


def login_user(request):
       if request.method=="POST":
           username=request.POST.get('username')
           password=request.POST.get('password')

           if not User.objects.filter(username=username).exists():
                messages.error(request,"Username is Invalid")
                return redirect('/login/')
           user=authenticate(username=username,password=password)
           if user is not None:
                 login(request,user)
                 return redirect("/add_recipe/")
           else:
                 messages.error(request,"Invalid Credential")
                 return redirect('/login/') 
           



           
       return render(request,"login.html")