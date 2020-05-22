from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

from .templates import pages

# Create your views here.
def HomePageView(request):
    all_list=Post.objects.all()
    return render(request,'pages/home.html',{'object_list': all_list})