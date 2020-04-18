from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm, MakePaymentForm
from .models import OrderLineItem
from django.conf import settings
from posts.models import Post
from django.utils import timezone
from django.template.loader import get_template
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
                product.initial_quantity = product.initial_quantity - quantity
                product.save()
                request.session['cart'] = {}
                subject = "Thank you for your order"
                from_email = settings.EMAIL_HOST_USER
                to_email = [request.user.email]
                with open(settings.BASE_DIR + "/templates/account/email/checkout.txt") as f:
                    checkout_message = f.read()
                message = EmailMultiAlternatives(subject=subject, body=checkout_message, from_email=from_email,
                    to=to_email)
                html_template = get_template("checkout_email.html").render()
                message.attach_alternative(html_template, "text/html")
                message.send()
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