from django.shortcuts import render ,redirect


def index(request):
    return render(request , 'myapp/index.html')

def result(request):
    if request.method == 'POST' :
        context = {
            'user_name' : request.POST['user_name'],
            'location' :request.POST['location'],
            'gender' : request.POST['gender'],
            'hobbies' :request.POST.getlist('hobbies'),
            'language' : request.POST['language']
        }

        return render (request , 'myapp/result.html' , context)
    return redirect ('/')
