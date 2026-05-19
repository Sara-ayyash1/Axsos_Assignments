from django.shortcuts import render , redirect

# Create your views here.
def index(request):   
    if 'visit' not in request.session:
        request.session['visit'] = 0
    if 'counter' not in request.session :
        request.session['counter'] = 0

    request.session['visit'] +=1
    return render(request , 'index.html')

def destroy_session(request):
    #request.session.flush()  # destroy session 
    del request.session['visit']    # clears a specific key
    del request.session['counter'] 
    return redirect('/')

def increment_count_2(request):
    if 'counter' in request.session :
        request.session['counter'] +=2
    return redirect('/')
    
def increment_by(request):
    if 'counter' in request.session :
        amount = int(request.POST['amount'])
        request.session['counter'] += amount
    return redirect('/')