from django.shortcuts import render, redirect
from .models import Project

def redirect_to_mypage(request):
    return redirect('/mypage/')

def home(request):
    return render(request, 'core/home.html')

def projects(request):
    projects = Project.objects.all().order_by('-date')
    return render(request, 'core/projects.html', {'projects':projects})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
