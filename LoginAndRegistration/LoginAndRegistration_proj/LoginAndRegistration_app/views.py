from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request , 'LoginAndRegistration_app/index.html')


def register(requsst):
    if requsst.method == 'POST':
        errors= User.objects.registration_validator(requsst.POST)

        if errors:
            for key, value in errors.items():
                messages.error(requsst,value)
            return redirect('/')  

        pw_hash = bcrypt.hashpw(requsst.POST['password'].encode() , bcrypt.gensalt() ).decode() 

        user = User.objects.create(
            first_name = requsst.POST['first_name'],
            last_name = requsst.POST['last_name'],
            email = requsst.POST['email'],
            password = pw_hash,
            birthday = requsst.POST['birthday']
        ) 

        requsst.session['user_id'] = user.id
        requsst.session['user_name'] = f" {user.first_name} {user.last_name}"

        return redirect('success')
    return redirect('/')

def login(request):
    if request.method =='POST':
        errors = User.objects.login_validator(request.POST)

        if errors:
            for key, value in errors.items():
                messages.error(request ,value)
            return redirect('/')  
         
        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] =user.id
        request.session['user_name'] = f" {user.first_name} {user.last_name}"
        return redirect('success')
    
    return redirect('/')

def success(request):
    if 'user_id' in request.session : 
        context = {
            "user_name" :request.session['user_name']
        }
        return render(request ,'LoginAndRegistration_app/success.html' , context)
    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')
