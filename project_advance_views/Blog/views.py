from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Blog
from .forms import PostForm

def blog(request):
    isi= Blog.objects.all()
    return render(request, 'blog/daftar_blog.html', {'isi':isi})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_blog')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form':form})
# Create your views here.
