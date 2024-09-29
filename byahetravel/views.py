from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'users/sign-in.html')

def sign_up(request):
    return render(request, 'users/sign-up.html')