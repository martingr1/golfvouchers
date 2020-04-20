from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required 
from .models import Post
from .forms import PostForm
from .filters import PostFilter


def get_posts(request):

    posts_list = Post.objects.filter(listed_date__lte=timezone.now()).order_by('listed_date')
    post_filter = PostFilter(request.GET, queryset=posts_list)
    posts_list = post_filter.qs

    p = Paginator(posts_list, 12)
    page = request.GET.get('page')
    try:
        posts = p.page(page)
    
    except PageNotAnInteger:
        posts = p.page(1)
    
    except EmptyPage:
        posts = p.page(p.num_pages)

    context = {
        'posts': posts, 'post_filter': post_filter,
}

    return render(request, "posts.html", context)


def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})


@login_required
def create_or_edit_post(request, pk=None):

    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    
    else:
        form = PostForm(instance=post)
    return render(request, 'postform.html', {'form': form})
