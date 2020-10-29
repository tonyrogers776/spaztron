from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def arma(request):
    return render(request, 'arma.html')

def dji(request):
    return render(request, 'dji.html')

# Create your views here.
