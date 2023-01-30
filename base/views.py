from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import  *
from .models import *
from django.core.mail import send_mail
from .forms import ContactForm


# Create your views here.

def home(request):
    return render(request,'home.html')

def comingsoon(request):
    return render(request, 'comingsoon.html' )

def about(request):
    return render(request,'aboutus.html')

def other(request):
    return render(request,'others.html')

# def loginPage(request):
#     if request.method =='POST':
#         username= request.POST.get('username').lower()
#         password= request.POST.get('password')  
       
#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request,"Username doesn't exist")
        
        
#         user = authenticate(request,username=username,password=password)

#         if user is not None:
#             login(request,user),
#             return render(request,'others.html')
#         else:
#             messages.error(request,"Username or password doesn't exist")
#     context={}
#     return render(request,'login.html',context)


# def signup(request):
#     form = MyUserCreationForm()

#     if request.method == 'POST':
#         form = MyUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return render(request,'others.html')
#         else:
#             messages.error(request,'An error occurred during registration')
#     return render(request, 'signup.html', {'form': form})
    

def movie(request, id):
    movie= Movie.objects.get(movie_id=id)
    # for i in Movie.objects.all():
    #     if i['id']==int(pk):
    #         movie=i
    context={'movie':movie}
    return render(request,'movie.html',context)

def contact(request):
    form = ContactForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            form.save()

    context= {'form': form }     
    return render(request, 'contact.html', context)

def reservation(request):
    form = ReservationForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            form.save() 
        context={movie}
        return render(request,'movies.html')
    context= {'form': form }     
    return render(request,'reservation.html',context)

def movies(request):
    context= {} 
    return render (request,'movies.html')


def movies(request):
    movies = Movie.objects.all()
    context= {"movies":movies} 
    return render (request,'movies.html', context)