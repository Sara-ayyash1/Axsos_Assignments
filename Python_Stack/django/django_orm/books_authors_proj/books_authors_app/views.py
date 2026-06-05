from django.shortcuts import render ,  redirect
from .models import *
# Create your views here.
def index(request):
    context = {
        "books" : Book.objects.all()
    }
    return render(request , 'book.html',context=context)

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(title = request.POST['title'] , desc =request.POST['desc'])
        return redirect('/')
    return redirect('/')


def book_detail(request , id):
    book = Book.objects.get( id = id)
    if request.method == "POST":
        author_id = request.POST['author_id']
        author = Author.objects.get(id=author_id)
        book.authors.add(author)
        return redirect(f'/book_detail/{id}')
    context = {
        'book' : book,
        'all_authors' : Author.objects.exclude(id__in = book.authors.all())
    }
    return render (request , "book_detail.html" , context=context )


def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
        return redirect('/')
    context = {'book': book}
    return render(request, 'edit_book.html', context=context)



def delete_book(request , id):
    book = Book.objects.get( id = id)
    book.delete()
    return redirect('/')

def authors_index(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render(request , 'author.html',context=context)

def add_author(request):
    if request.method == 'POST':
        Author.objects.create(first_name = request.POST['first_name'] , last_name =request.POST['last_name'] , notes = request.POST['notes'])
        return redirect('/authors')
    return redirect('/authors')

def author_detail(request , id):
    author = Author.objects.get( id = id)  
    if request.method == "POST":
        book_id = request.POST['book_id']
        book = Book.objects.get(id=book_id)
        author.books.add(book)
        return redirect(f'/author_detail/{id}')
    context = {
        'author': author,
        'all_books' : Book.objects.exclude(id__in= author.books.all())
    }
    return render (request , "author_detail.html" ,  context=context )
