from django.shortcuts import render
from django.http import HttpResponse
from .models import femalesinger
from .models import malesinger

# Create your views here.

def home(request):

    alphabatname = femalesinger.objects.all()
    alphabatname2 = malesinger.objects.all()
    return render(request, 'home.html', {'alphabatname':alphabatname, 'alphabatname2':alphabatname2})

def hdvideos(request):
    return render(request, 'hdvideos.html')

def contactus(request):
    return render(request, 'contactus.html')

def sites(request):
    return render(request, 'sites.html')

def categories(request):
    return render(request, 'categories.html')

def music(request):
    return render(request, 'music.html')

def upcoming(request):
    return render(request, 'upcoming.html')