from django.shortcuts import render
from .models import Post
from blog.forms import PostForm

def home(request):
    form=PostForm()
    return render(request,'blog/home.html',{'form':form})