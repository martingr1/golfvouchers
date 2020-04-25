from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User


class TestLoginForms(TestCase):
    def test_username_required(self):
        form = UserLoginForm({'password': "password"})
        self.assertFalse(form.is_valid())
        print(form.errors['username'], ['This field is required.'])
    
    def test_password_required(self):
        form = UserLoginForm({'username': 'admin'})
        self.assertFalse(form.is_valid())
        print(form.errors['password'], ['This field is required.'])
    
    def test_login_form(self):
        form = UserLoginForm({
            'username': 'martingr1',
            'password': 'password'
        })
        self.assertTrue(form.is_valid())
    
    def test_registration_passwords(self):

        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'password1',
            'password2': 'password1'
        })

        self.assertTrue(form.is_valid())
    
    def test_registration_email_must_be_unique(self):
        User.objects.create_user(
            username='testuser',
            email='test@test.com')

