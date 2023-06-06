from django.shortcuts import render
from .models import Book, Comment
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    categories = ['Category 1', 'Category 2', 'Category 3']  # Example categories
    books = Book.objects.all()
    context = {
        'categories': categories,
        'books': books
    }
    return render(request, 'home.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the desired URL after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with the desired URL after successful login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def booklet(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        # Handle comment submission
        content = request.POST.get('content')
        rated = int(request.POST.get('rated'))

        comment = Comment(book=book, buyer=request.user, content=content, rated=rated)
        comment.save()

        return redirect('booklet', book_id=book_id)

    context = {
        'book': book,
    }

    return render(request, 'booklet.html', context)