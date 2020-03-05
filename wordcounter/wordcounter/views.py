from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    full_text=request.GET['fulltext']
    no_full_text=len(full_text.split())
    return render(request,'count.html',{'fulltext':full_text,'no_words':no_full_text})