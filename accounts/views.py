from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import Context
from django.template.loader import get_template, render_to_string
from accounts.forms import UserLoginForm, UserRegistrationForm


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('get_posts'))
    else:
        return render(request,  'index.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,  "You have successfully been logged out.")
    return redirect(reverse('get_posts'))


def login(request):
    
    if request.user.is_authenticated:
        return redirect(reverse('get_posts'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password = request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('get_posts'))
            
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse, ('get_posts'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'], password =request.POST['password1'])
        
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered with GolfVouchers! Please log in.")
                user = request.user.username
                context = {"user": user}
                subject = "Thank you for registering with Golf Vouchers"
                from_email = settings.EMAIL_HOST_USER
                to_email = [request.user.email]
                with open(settings.BASE_DIR + "/templates/account/email/sign_up.txt") as f:
                    signup_message = f.read()
                message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email,
                    to=to_email)
                html_template = get_template("sign_up.html").render(context)
                message.attach_alternative(html_template, "text/html")
                message.send()
                return redirect(reverse('login'))
            else:
                messages.error(request, "Sorry, we were unable to register your account")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'register.html', {"registration_form": registration_form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user})


