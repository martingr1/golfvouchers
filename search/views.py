from django.shortcuts import render
from django.contrib import messages
from posts.models import Post


def do_search(request):
    
    posts = Post.objects.filter(content__icontains=request.GET['q']).order_by('listed_date')
    return render(request, "posts.html", {'posts': posts})
