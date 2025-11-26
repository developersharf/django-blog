from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Home Page!")
    # return render(request, 'home.html')
    
    
def post_list(request):
    return render(request, 'core/post_list.html', {})