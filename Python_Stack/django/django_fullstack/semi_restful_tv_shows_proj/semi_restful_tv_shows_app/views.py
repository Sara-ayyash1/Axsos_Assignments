from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages

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
        errors = Show.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/new/')
        
        else:
            new_show = Show.objects.create(
                title = request.POST['title'].strip(),
                network = request.POST['network'].strip(),
                release_date = request.POST['release_date'],
                description = request.POST['description'].strip()
            )
            messages.success(request, "Show successfully created.")
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
    if request.method == 'POST':
        # Pass the POST data to the method we wrote and save the response in a variable called errors.
        errors = Show.objects.basic_validator(request.POST , show_id)

        # Check if the errors dictionary has anything in it.
        if len(errors) > 0:
            # If the errors dictionary contains anything, loop through each key-value pair and make a flash message.
            for key, value in errors.items():
                messages.error(request, value)
            # Redirect the user back to the form to fix the errors.
            return redirect(f'/shows/{show_id}/edit/')
        
        else:
            # If the errors dictionary is empty, that means there were no errors.
            # Retrieve the Show to be updated, make the changes, and save.
            show_to_update = Show.objects.get(id = show_id)
   
            show_to_update.title = request.POST['title']
            show_to_update.network = request.POST['network']
            show_to_update.release_date = request.POST['release_date']
            show_to_update.description = request.POST['description']
            show_to_update.save()
            
            messages.success(request, "Show successfully updated.")
            # Redirect to a success route.
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