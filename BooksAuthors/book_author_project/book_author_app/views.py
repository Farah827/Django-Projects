from django.shortcuts import render ,redirect

from .models import *

def index(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request , 'book_author_app/index.html' ,context)

def create_book(request):
    if request.method =='POST':
        new_book = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc']
        )

        return redirect('/')
    return redirect('/')

def book_details(request , id):
    book = Book.objects.get(id=id)
    available_authors = Author.objects.exclude(books=book)
    context={
        'book':book,
        'authors':available_authors
    }
    return render(request , 'book_author_app/book_details.html' ,context)



def add_author_to_book(request ,id):
    book= Book.objects.get(id=id)
    if request.method == 'POST':
        author_id= request.POST['author']
        new_author=Author.objects.get(id=author_id)
        book.authors.add(new_author) 

    return redirect('book_details' , id =book.id)
    


def author(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request , 'book_author_app/author.html' ,context)

def create_author(request):
    if request.method == 'POST':
        Author.objects.create(
            first_name = request.POST['first_name'],
            last_name =request.POST['last_name'],
            notes = request.POST['notes']
        )
    return redirect('author')

def author_details(request ,id):
    context = {
        'author':Author.objects.get(id=id),
        'books':Book.objects.all()
    }
    return render(request , 'book_author_app/author_details.html' ,context)


def add_book_to_author(request ,id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        book_id = request.POST['book']
        new_book = Book.objects.get(id=book_id)
        author.books.add(new_book)

    return  redirect('author_details' , id=author.id)    

