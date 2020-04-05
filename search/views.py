from django.shortcuts import render
from posts.models import Post


def do_search(request):
    
    posts = Post.objects.filter(content__icontains=request.GET['q'])
    return render(request, "posts.html", {'posts': posts})

# Create your views here.
