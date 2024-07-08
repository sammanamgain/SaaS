from django.http import HttpResponse
from django.shortcuts import render
from visit.models import Visit
def home(request,*args):
    context={'title':"homePage"}
    Visit.objects.create()

  
    return render(request,'home.html',context)