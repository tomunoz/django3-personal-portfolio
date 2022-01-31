from django.shortcuts import render
from .models import(School)
from .models import(Interest)
from .models import(Company)
from .models import(Social)

# Create your views here.


def about(request):
    schools = School.objects.all()
    interests = Interest.objects.all()
    companies = Company.objects.all()
    socials = Social.objects.all()
    return render(request, 'about/about.html', {'schools':schools, 'interests':interests, 'companies':companies, 'socials': socials})


