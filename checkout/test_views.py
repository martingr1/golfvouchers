from django.test import TestCase
from .models import Order, OrderLineItem
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages


class TestCheckoutViews(TestCase):

    def test_get_checkout(self):

        User.objects.create_user(

            username='testname',
            email="test@test.com",
            password="password1",
        )

        self.client.login(username="testname", password="password1")

        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)

    def test_payment_accepted(self):

        User.objects.create_user(

            username='testname',
            email="test@test.com",
            password="password1",
        )

        self.client.login(username="testname", password="password1")

        response = self.client.post("/checkout/", {

            "credit_card_number": "4242424242424242",
            "cvv": "111",
            "expiry_month": "6",
            "expiry_year_": "2025",
        }, follow=True)

        for message in get_messages(response):
            self.assertNotEqual("Your card was declined", messages)
        
        page = self.client.get("/posts/")
        self.assertEqual(page.status_code, 200)

    def test_card_declined(self):

        User.objects.create_user(

            username='testname',
            email="test@test.com",
            password="password1",
        )

        self.client.login(username="testname", password="password1")

        response = self.client.post("/checkout/", {

            "credit_card_number": "4242424242424242",
            "cvv": "111",
            "expiry_month": "6",
            "expiry_year_": "2025",
        }, follow=True)

        for message in get_messages(response):
            self.assertEqual("Your card was declined!", messages)
        
        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout.html")
