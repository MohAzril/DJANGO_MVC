from django.shortcuts import render

def blog(request):
    return render(request, 'blog/daftar_blog.html',{})
# Create your views here.
