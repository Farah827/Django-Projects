from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request , 'wall_app/index.html')


def register(request):
    if request.method == 'POST':
        errors= User.objects.registration_validator(request.POST)

        if errors:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')  

        pw_hash = bcrypt.hashpw(request.POST['password'].encode() , bcrypt.gensalt() ).decode() 

        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash,
        ) 

        request.session['user_id'] = user.id
        request.session['user_name'] = f" {user.first_name} {user.last_name}"

        return redirect('home_page')
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
        return redirect('home_page')
    
    return redirect('/')

def home_page(request):
    if 'user_id' in request.session : 
        context = {
            "user_name" :request.session['user_name'],
            "posts" : Post.objects.all().order_by('-created_at'),
            
        }
        return render(request ,'wall_app/home_page.html' , context)
    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')


def post_message(request):
    if request.method == 'POST' and 'user_id' in request.session :
        Post.objects.create(
            post = request.POST['post'],
            user = User.objects.get(id=request.session['user_id'])

        )

    return redirect('home_page')


def add_comment(request ,post_id):
    if request.method == 'POST':

        post= Post.objects.get(id = post_id)
        user = User.objects.get(id = request.session['user_id'])

        Comment.objects.create(
            comment = request.POST['comment'],
            post = post,
            user = user

        )
        return redirect('home_page')
    return redirect('home_page')
