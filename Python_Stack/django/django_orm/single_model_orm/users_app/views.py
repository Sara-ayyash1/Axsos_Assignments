from django.shortcuts import render , redirect
from .models import Users

# Create your views here.
def index(request):
    context = {
        "users" : Users.objects.all()
    }
    return render(request , "index.html" , context)

def add_user(request):
    Users.objects.create(first_name = request.POST.get('first_name') ,
                        last_name = request.POST.get('last_name'),
                        email_address =request.POST.get('email'),
                        age =  request.POST.get('age') )
    return redirect('/')