from django.shortcuts import render , redirect 

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def process_form(request):
    context = {
        'name':     request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'level':    request.POST['level'],
        'comment':  request.POST.get('comment')  or 'No Comment',
    }
    return render(request, 'info.html', context)
