from django.shortcuts import render

def author(request):
    return render(request, 'author/daftar_author.html',{})
# Create your views here.
