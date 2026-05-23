from django.shortcuts import render, redirect
import random     

def get_message_style(message):
    if not message:
        return {'bg': '', 'text': ''}
    if 'high' in message:
        return {'bg': 'bg-red-50 border-red-100', 'text': 'text-red-600'}
    elif 'low' in message:
        return {'bg': 'bg-blue-50 border-blue-100', 'text': 'text-blue-600'}
    elif 'Correct' in message:
        return {'bg': 'bg-green-50 border-green-100', 'text': 'text-green-700'}
    else:
        return {'bg': 'bg-gray-50 border-gray-100', 'text': 'text-gray-600'}
    
def index(request):
    if 'answer' not in request.session:
        request.session['answer'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['message'] = None
        request.session['game_over'] = False
        
    if 'winners' not in request.session:
        request.session['winners'] = []

    attempts = request.session.get('attempts', 0)
    width_percentage = (attempts / 5) * 100
    style = get_message_style(request.session.get('message'))
    
    context = {
        'bg': style['bg'],
        'text': style['text'],
        'width': width_percentage
    }
    return render(request, 'index.html', context)

def process(request):
    if request.method == "POST":
        if request.session.get('game_over'):
            return redirect('/')
        
        user_ans = int(request.POST['guessing_num'])
        request.session['attempts'] += 1
        
        if user_ans > request.session['answer']:
            request.session['message'] = "Too high!"
        elif user_ans < request.session['answer']:
            request.session['message'] = "Too low!"
        else:
            request.session['message'] = f"Correct! {request.session['answer']} was the number!"
            request.session['game_over'] = True
            return redirect('/')

        if request.session['attempts'] >= 5 and not request.session['game_over']:
            request.session['message'] = 'You Lose! Game Over'
            request.session['game_over'] = True

    return redirect('/')

def reset(request):
    request.session.flush() 
    return redirect('/')

def submit_winner(request):
    if request.method == 'POST':
        name = request.POST['name']
        attempts = request.session.get('attempts', 0)
        
        current_winners = request.session.get('winners', [])
        current_winners.append({'name': name, 'attempts': attempts})
        request.session['winners'] = current_winners
        request.session.modified = True

        if 'answer' in request.session:
            del request.session['answer']
        request.session['attempts'] = 0
        request.session['message'] = None
        request.session['game_over'] = False
        
        return redirect('/leaderboard')
    return redirect('/')

def leaderboard(request):
    winners_list = request.session.get('winners', [])
    sorted_winners = sorted(winners_list, key=lambda x: x['attempts'])
    
    return render(request, 'leaderboard.html', {'winners': sorted_winners})

