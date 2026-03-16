# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        return redirect('all_chai')
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('all_chai')
        else:
            return render(request, 'index.html', {'error': 'Invalid credientials', 'form': 'login'})
    return redirect('index')
    
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')
        if password != confirm:
            return render(request, 'index.html', {'error': 'Passwords do not match', 'form': 'signup'})
        if User.objects.filter(username=username).exists():
            return render(request, 'index.html', {'error': 'Username already taken', 'form': 'signup'})
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('all_chai')
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')

