from django.shortcuts import render , redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request , 'index.html' ,context=context)

def add_course(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)

        if len(errors ) >0:
            for key , value in errors.items() :
                messages.error(request , value)
            return redirect('/')
        else:
           new_course =  Course.objects.create(name = request.POST.get('name').strip())
           Description.objects.create(content = request.POST.get('description').strip() , course = new_course)
           messages.success(request, "Course successfully created.")
           return redirect('/')

    return redirect('/')


def destroy_course(request, course_id):
    course_to_delete = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course_to_delete.delete()
        return redirect('/')
  
    context = {
        'course': course_to_delete
    }
    return render(request, 'delete_confirm.html', context)

def new_comment(request , course_id):
    course = Course.objects.get(id = course_id)
    context = {
        'course' : course ,
        'all_comments' : course.comments.all()
    }
    return render(request , 'comment.html' , context=context)

def create_comment(request, course_id):
    course = Course.objects.get(id = course_id)
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if len(content) == 0:
            messages.error(request, "Comment cannot be empty!")
            return redirect('new_comment', course_id=course_id)
        Comment.objects.create(content = content , course = course)
        return redirect('new_comment' , course_id =course_id)
    return redirect('new_comment' ,course_id =course_id)
