from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class TestProductViews(TestCase):

    def test_get_product_page(self):

        user = User.objects.create_user(

            username='testname',
            email="test@test.com",
            password="password1",
        )

        self.client.login(username="testname", password="password1")
        page = self.client.get("/posts/")
        self.assertEqual(page.status_code, 200)

    