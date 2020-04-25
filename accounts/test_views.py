from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestLoginView(TestCase):

    def test_get_login_form(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
    
    def test_login(self):

        user1 = User.objects.create_user(

            username='testname',
            email="test@test.com",
            password="password1",
        )

        response = self.client.post("/accounts/login/",{

            "username": "testname",
            "password": "password1"

        })

        response = self.client.get("/accounts/login/")
    
    def test_user_does_not_exist(self):

        response = self.client.post("/accounts/login/", {

            "username":"testuser",
            "password":"password1"

        })

        self.assertFormError(response, "login_form", None, "Your username or password is incorrect")

    
    def test_registration_form_invalid(self):

        response = self.client.post("/accounts/register/", {

            "username":'testname',
            "email":"test@test.com",
            "password1":"password1",
            "password2":"password2",
        })
        self.assertEqual(User.objects.count(), 0)
