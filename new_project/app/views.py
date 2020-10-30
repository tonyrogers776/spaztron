from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def arma(request):
    return render(request, 'arma.html')

def dji(request):
    return render(request, 'dji.html')

def contact(request):
    return render(request, 'contact.html')

def photos(request):
    return render(request, 'photos.html')

# Create your views here.
