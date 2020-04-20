from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post
from posts.filters import PostFilter


def do_search(request):
    
    posts_list = Post.objects.all()
    query = request.GET.get('q')

    post_filter = PostFilter(request.GET, queryset=posts_list)
    posts_list = post_filter.qs

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
            'posts': posts, 'post_filter': post_filter, }

    return render(request, "posts.html", context)
