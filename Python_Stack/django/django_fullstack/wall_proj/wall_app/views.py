from django.shortcuts import render ,redirect
from login_app.models import User
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user , 
        'all_messages' : Message.objects.all().order_by('-created_at') , 

    }
    return render(request , 'wall.html' , context)


def create_message(request ):
    if request.method == 'POST':
        if 'user_id' not in request.session:
           return redirect('/')
        
        user = User.objects.get(id=request.session['user_id'])
        Message.objects.create(message = request.POST.get('message' , '').strip() , user =  user)
        return redirect('/wall')
    return redirect('/wall')

def create_message(request):
    if request.method == 'POST':
        if 'user_id' not in request.session:
            return redirect('/')
        
        errors = Message.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/wall')
        
        user = User.objects.get(id=request.session['user_id'])
        Message.objects.create(
            message=request.POST.get('message', '').strip(), 
            user=user
        )
        return redirect('/wall')
        
    return redirect('/wall')


def create_comment(request):
    if request.method == 'POST':
        if 'user_id' not in request.session:
            return redirect('/')
            
        message_id = request.POST.get('message_id')
        if not message_id:
            return redirect('/wall')
            
        errors = Comment.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/wall')
            
        try:
            user = User.objects.get(id=request.session['user_id'])
            message = Message.objects.get(id=int(message_id))
            
            Comment.objects.create(
                comment=request.POST.get('comment', '').strip(), 
                user=user, 
                message=message
            )
        except (Message.DoesNotExist, ValueError):
            messages.error(request, "Something went wrong. Post not found.")
            
        return redirect('/wall')
        
    return redirect('/wall')

def delete_message(request, message_id):
    if 'user_id' not in request.session:
        return redirect('/')
        
    if request.method == 'POST': 
        try:
            message_to_delete = Message.objects.get(id=message_id)
            
            if message_to_delete.user.id != request.session['user_id']:
                messages.error(request, "You can only delete your own messages!")
                return redirect('/wall')
                
            delete_errors = Message.objects.validate_delete(message_id)
            
            if len(delete_errors) > 0:
                for key, value in delete_errors.items():
                    messages.error(request, value)
                return redirect('/wall')
                
            message_to_delete.delete()
            messages.success(request, "Message deleted successfully.") 
            
        except Message.DoesNotExist:
            messages.error(request, "Message already deleted or doesn't exist.")
            
    return redirect('/wall')