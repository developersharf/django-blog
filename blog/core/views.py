from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Home Page!")
    # return render(request, 'home.html')
    
    
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'core/post_list.html', {'posts': posts})