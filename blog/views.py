from django.shortcuts import render
from blog.models import BlogPost, Author, Topic

# Create your views here.

def index(request):
    '''View function for the homepage'''

    return render(request, 'index.html')

