from django.db import models


CATEGORY_CHOICES = (
    ('bags', 'Bags'),
    ('balls', 'Balls'),
    ('dmd', 'DMD'),
    ('gloves', 'Gloves'),
    ('grips', 'Grips'),
    ('other', 'Other'),

)


class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    listed_date = models.DateTimeField(auto_now_add=True)
    initial_quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='balls')
    manufacturer = models.CharField(max_length=25, blank=True, null=True, default='manufacturer')
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    def __unicode__(self):
        return self.title
