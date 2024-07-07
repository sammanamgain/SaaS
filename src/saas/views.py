from django.http import HttpResponse
from django.shortcuts import render
def home(request,*args):
    context={'title':"homePage"}

  
    return render(request,'home.html',context)