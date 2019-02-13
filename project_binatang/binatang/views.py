from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Hewan
from .forms import PostForm



def daftar_binatang(request):
    binatang= Hewan.objects.all()
    return render(request, 'binatang/daftar_binatang.html', {'hewan':binatang}) #'hewan' keyword di html
    # return render(request, 'binatang/daftar_binatang.html',{}),

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_binatang')
    else:
        form = PostForm()
    return render(request, 'binatang/post_new.html', {'form':form}) 

def db_binatang(request):
    binatang= Hewan.objects.all()
    return render(request, 'binatang/db_binatang.html', {'hewan':binatang})
# Create your views here.
