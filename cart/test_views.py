from django.test import TestCase
from posts.models import Post
from django.contrib.auth.models import User


class TestCartViews(TestCase):

    def test_get_cart(self):
        User.objects.create_user(
            username='testname',
            email="test@test.com",
            password="password1")
        
        self.client.login(username="testname", password="password1")
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
    
    def test_add_to_cart(self):
        User.objects.create_user(
            username='testname',
            email="test@test.com",
            password="password1")
        self.client.login(username="testname", password="password1")
        product = Post.objects.create(title="test product",
        content="test", price="10.99", manufacturer="Titleist", initial_quantity="10", category="balls")

        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get("/posts/1".format(Post.pk))

        session = self.client.session
        session['user_cart'] = 'cart_session'

        response = self.client.post("/cart/",
                                    kwargs={'product_id': product.id})
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)