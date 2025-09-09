from django.shortcuts import render , redirect
import random

def index(request):
    if 'number' not in request.session :
        request.session['number'] = random.randint(1,100)
        request.session['attempts'] = 0
        request.session['game_over'] =False
        request.session['message'] =''

    context = {
        'attempts' :  request.session['attempts'],
        'game_over': request.session['game_over'],
        'message' :  request.session['message']
    } 

    return render(request , 'game_app/index.html' , context)   


def guess(request):
    if request.method == 'POST':
        if request.session.get('game_over', False):
            return redirect('/')

        guess = int(request.POST['guess']) 
        number = int(request.session['number'])
        attempts = int(request.session['attempts'])
        request.session['attempts'] += 1
        print(f"******************************** {request.session['number']} *********************")

    
        if(guess < number):
            request.session['message'] = "Too Low !"  
 
        elif(guess > number):
            request.session['message'] = "Too High!"

        else:
            request.session['message'] =  f"YOU win ! The number was {number}"
            request.session['game_over'] = True 
            return redirect('/')

        if  request.session['attempts'] >= 5 and not request.session['game_over']:
            request.session['message'] =  f"You Lose! The number was {number}." 
            request.session['game_over'] =True
            
    return redirect('/')          


def reset(request):
    request.session.flush()
    return redirect('/')


leaders=[]
def winners(request):    
    if request.method == 'POST':  
        winner_name = request.POST['winnerName']
        attempts = request.session['attempts']

        leaders.append({
            "name": winner_name, 
            "attempts": attempts
        })


    context = {
        'leaders': leaders
    }
    return render(request, 'game_app/leaderboard.html', context)
    

def leaderboard(request):
    context = {
        'leaders' : leaders
        }
    return render(request , 'game_app/leaderboard.html' ,context)