from django.shortcuts import render
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'base.html' ,{
        'media_url': settings.MEDIA_URL})

def login(request):
    return render(request, 'login.html')

def products(request):
    return render(request, 'products.html')

def camera(request):
    return render(request, 'camera.html')
