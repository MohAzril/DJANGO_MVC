from django.shortcuts import render
from django.utils import timezone
from .models import Mentee

def mentee(request):
    mentee= Mentee.objects.all()
    return render(request, 'mentee/daftar_mentee.html',{'mentee':mentee})
# Create your views here.
