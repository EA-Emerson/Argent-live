from doctest import FAIL_FAST
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

from mylist import settings

# create your views here
def home(request):
    return render(request, "homepage/index.html")

def signup(request):
    if request.method == "POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
    
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists. Please try another username")
            return redirect("signup")
            
        if User.objects.filter(email=email):
            messages.error(request, 'Email already registered')
            return redirect('signup')
        
        if len(username)>15:
            messages.error(request, "Username must be under 10 characters")
            return redirect('signup')
            
        if pass1 != pass2:
            messages.error(request, "Passwords don't match")
            return redirect('signup')
            
        if not username.isalnum():
            messages.error(request, "Username must be alpha numeric")
            return redirect('signup')
    
        my_user=User.objects.create_user(username, email, pass1)
        my_user.first_name=fname
        my_user.last_name=lname
        # my_user.is_active=False
        my_user.save()
        
        messages.success(request, 'Your account has been successfully created. We have sent you a confirmation email, please confirm your email in order to activate your account')
        
        
        # Welcome Email
        # subject='Welcome to Argent!'
        # message="Hello " + my_user.first_name + "!! \n Welcome to ARGENT!! \n Thank you for visiting our website \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thanking you \n Team Argent"
        # from_email=settings.EMAIL_HOST_USER
        # to_list=[my_user.email]
        # send_mail(subject, message, from_email, to_list, FAIL_FAST)
        
        
        return redirect('signin')
        
    return render(request, "accounts/signup.html")

def signin(request):
    if request.method =='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        
        user=authenticate(username=username, password=pass1)
    
        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, "homepage/index.html", {'fname':fname})
            
        else:
            messages.error(request, "Bad credentials")
            return redirect('signin')
            # return render(request, "accounts/signin.html")
        

    return render(request, "accounts/signin.html")

def signout(request):
    # return render(request, "accounts/signup.html")
    logout(request)
    messages.success(request, 'logged out successfully')
    return redirect('home')