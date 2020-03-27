from django.shortcuts import render
from .models import Blog

def allblog(request):
    blog=Blog.objects
    return render(request,'blog/blog.html',{'blog':blog})
