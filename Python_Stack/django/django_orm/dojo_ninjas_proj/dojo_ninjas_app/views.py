from django.shortcuts import render , redirect
from .models import Dojo ,Ninja

# Create your views here.
def index (request):
    context = {
        'all_dojo' :Dojo.objects.all()
    }
    return render(request , 'index.html' , context = context)

def add_dojo(request):
    Dojo.objects.create(name = request.POST.get('name') , city = request.POST.get('city') , state = request.POST.get('state'))
    return redirect('/')


def add_ninja(request):
    dojo = Dojo.objects.get(id=request.POST.get('dojo'))
    Ninja.objects.create(
        first_name = request.POST.get('first_name'),
        last_name = request.POST.get('last_name'),
        dojo = dojo
    )
    return redirect('/')

def delete_dojo(request, dojo_id):
    Dojo.objects.get(id=dojo_id).delete()
    return redirect('/')