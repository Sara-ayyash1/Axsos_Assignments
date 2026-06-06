from django.shortcuts import render , redirect
from .models import *
# Create your views here.
def index(request):
    context ={
        'all_shows' : Show.objects.all()
    }
    return render(request , 'index.html' , context=context)


def new_show(request):
    return render(request, 'add_show.html')


def create_show(request):
    if request.method == 'POST':
        new_show = Show.objects.create(
            title = request.POST['title'], 
            network = request.POST['network'],
            release_date = request.POST['release_date'], 
            description = request.POST['description']
        )
        return redirect(f'/shows/{new_show.id}')
    
    return redirect('/shows/new/') 


def show_detail(request , show_id ):
   show = Show.objects.get(id = show_id)
   context = {
       'show' : show
   }
   return render(request , 'show_detail.html' , context=context)


def destroy_show(request , show_id):
    Show.objects.get(id = show_id).delete()
    return redirect('/shows')


def edit_show(request , show_id):
    show = Show.objects.get(id = show_id)
    return render(request, 'edit_show.html' , context={'show' : show})


def update_show(request, show_id):
    show_to_update = Show.objects.get(id = show_id)
    if request.method == 'POST':    
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.description = request.POST['description']
        show_to_update.save()
        
        return redirect(f'/shows/{show_id}')
    
    return redirect(f'/shows/{show_id}/edit/')


# from django.utils import timezone
# def update_show(request, show_id):
#     if request.method == 'POST':    
#         Show.objects.filter(id=show_id).update(
#             title = request.POST['title'],
#             network = request.POST['network'],
#             release_date = request.POST['release_date'],
#             description = request.POST['description'],
#             updated_at = timezone.now()
#        )       
#         return redirect(f'/shows/{show_id}')
    
#     return redirect(f'/shows/{show_id}/edit/') 