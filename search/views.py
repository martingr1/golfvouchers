from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post


def do_search(request):
    
    posts_list = Post.objects.all()
    query = request.GET.get('q')

    if query:

        posts_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()

    p = Paginator(posts_list, 12)
    page = request.GET.get('page')

    try:
        posts = p.page(page)
    
    except PageNotAnInteger:
        posts = p.page(1)
    
    except EmptyPage:
        posts = p.page(p.num_pages)

    context = {
            'posts': posts}

    return render(request, "posts.html", context)
