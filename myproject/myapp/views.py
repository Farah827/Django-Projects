from django.shortcuts import render 
from django.http import HttpResponse ,request
from time import gmtime , strftime ,localtime
from datetime import datetime

def index(request):
    current_time = datetime.now()
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "date": current_time.strftime("%B %d, %Y"), 
        "clock": current_time.strftime("%I:%M %p")
    }
    return render(request,'myapp/time_display.html', context)


def way2(request):
    context = {
        "time": strftime("%Y-%m-%d" ,localtime()),
        "date": strftime("%H:%M %p" ,localtime())
    }
    return render(request ,'myapp/way2.html' ,context)
    
