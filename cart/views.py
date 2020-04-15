from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post


@login_required
def view_cart(request):
    return render(request, "cart.html")


@login_required
def add_to_cart(request, id):

    product = get_object_or_404(Post, pk=id)
    initial_quantity = product.initial_quantity
    quantity = int(request.POST.get('quantity'))

    if initial_quantity == 0:
        messages.error(request,  "Sorry, that item is sold out")
        return redirect(reverse('index'))
    elif quantity > initial_quantity:
        messages.error(request,  "Sorry, not enough items in stock to fulfill request")
        return redirect(reverse('index'))
    else:
        cart = request.session.get('cart', {})
        cart[id] = cart.get(id, quantity)
        request.session['cart'] = cart
        return redirect(reverse('index'))


@login_required
def adjust_cart(request, id):
  
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))