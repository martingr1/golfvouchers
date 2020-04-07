from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm, MakePaymentForm
from .models import OrderLineItem
from django.conf import settings
from posts.models import Post
from django.utils import timezone
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required
def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Post, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order= order,
                    post= product, 
                    quantity= quantity)
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined")
            
            if customer.paid:
                messages.error(request, "Transaction complete")
                request.session['cart'] = {}
                return redirect(reverse('get_posts'))

            else:
                messages.error(request, "Unable to take payment")
        else: 
            print(payment_form.errors)
            print(payment_form)
            messages.error(request, "Unable to take payment from card, please try another payment method")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    return render(request, "checkout.html", {'order_form':order_form, 'payment_form': payment_form,
    'publishable': settings.STRIPE_PUBLISHABLE})
