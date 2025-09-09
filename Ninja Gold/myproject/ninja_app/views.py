from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninja_app/index.html', 
    {
        'gold': request.session['gold'],
        'activities': request.session['activities']
    })


def process_money(request):
    if request.method == 'POST':
        location = request.POST['location']
        earned_gold = 0
        activities = request.session['activities']

        if location == 'farm':
            earned_gold = random.randint(10, 20)
        elif location == 'cave':
            earned_gold = random.randint(10, 20)
        elif location == 'house':
            earned_gold = random.randint(10, 20)
        elif location == 'quest':
            earned_gold = random.randint(-50, 50)

        request.session['gold'] += earned_gold

        if earned_gold > 0:
            activity = f"You earned {earned_gold} gold from the {location}!"
        else:
            activity = f"You lost {earned_gold} gold on a {location} quest..."

        activities.append(activity)
        request.session['activities'] = activities

    return redirect('/')




