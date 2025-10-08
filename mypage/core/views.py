from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all().order_by('-date')
    return render(request, 'core/home.html', {'projects':projects})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
