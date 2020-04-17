from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post


def do_search(request):
    
    posts_list = Post.objects.filter(content__icontains=request.GET['q']).order_by('listed_date')
    p = Paginator(posts_list, 1)
    page = request.GET.get('page')
    try:
        posts = p.page(page)
    
    except PageNotAnInteger:
        posts = p.page(1)
    
    except EmptyPage:
        posts = p.page(p.num_pages)

    return render(request, "posts.html", {'posts': posts})
