from django.db import models
from posts.models import Post


class Order(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    contact_number = models.CharField(max_length=30, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=50, blank=False)
    street_address_1 = models.CharField(max_length=50, blank=False)
    street_address_2 = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=50, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.first_name, self.last_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False,  related_name="line_items")
    post = models.ForeignKey(Post, null=False,  related_name="orders")
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.post.title, self.post.price)

