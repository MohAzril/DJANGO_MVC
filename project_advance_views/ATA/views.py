from django.shortcuts import render

def home(request):
    return render(request, 'home/daftar_home.html',{})
# Create your views here.
