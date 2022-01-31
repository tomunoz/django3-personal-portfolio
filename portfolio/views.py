from django.shortcuts import render
from .models import(Project)
from about.models import(Social)

# Create your views here.


def home(request):
    projects = Project.objects.all()
    socials = Social.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects, 'socials':socials})