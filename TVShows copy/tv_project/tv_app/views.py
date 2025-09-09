from django.shortcuts import render

from django.shortcuts import render ,redirect
from .models import *

def index(request):
    context = {
        "shows": Show.objects.all()
    }
    
    return render(request, 'tv_app/index.html' ,context)


def create_show(request):
    if request.method == 'POST':
        title = request.POST['title']
        network =request.POST['network']
        release_date=request.POST['release_date']
        desc=request.POST['desc']

        new_show=Show.objects.create(title=title ,network=network ,release_date=release_date,desc=desc)

        return redirect('show_details', id=new_show.id)
    return render(request , 'tv_app/create.html')


def show_details(request ,id):
    show = Show.objects.get(id=id)
    context = {
        "shows" : show,
    }
    return render(request ,'tv_app/show_details.html' ,context )


def edit_show(request,id):
    old_show = Show.objects.get(id=id)
    if request.method == 'POST':
        old_show = Show.objects.get(id=id)

        old_show.title= request.POST['title']
        old_show.network= request.POST['network']
        old_show.release_date= request.POST['release_date']
        old_show.desc= request.POST['desc']
        old_show.save()

        return redirect("show_details" , id=old_show.id)
    return render(request, 'tv_app/edit_show.html', {'show': old_show})


def delete_show(request , id):
    delete_show=Show.objects.get(id=id)
    delete_show.delete()
    return redirect('index')

