from django.shortcuts import render
from django.utils import timezone
from .models import Mentor

def mentor(request):
    mentor= Mentor.objects.all()
    return render(request, 'mentor/daftar_mentor.html',{'mentor':mentor})
# Create your views here.
