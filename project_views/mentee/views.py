from django.shortcuts import render

def mentee(request):
    return render(request, 'mentee/daftar_mentee.html',{})
# Create your views here.
