from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('bags', 'Bags'),
    ('balls', 'Balls'),
    ('dmd', 'DMD'),
    ('gloves', 'Gloves'),
    ('grips', 'Grips'),
    ('other', 'Other'),

)

MANUFACTURER_CHOICES = (

    ('aldila', 'Aldila'),
    ('ben hogan', 'Ben Hogan'),
    ('bridgestone', 'Bridgestone'),
    ('callaway', 'Callaway'),
    ('cleveland', 'Cleveland'),
    ('cobra', 'Cobra'),
    ('footjoy', 'Footjoy'),
    ('lamkin', 'Lamkin'),
    ('mizuno', 'Mizuno'),
    ('odyssey', 'Odyssey'),
    ('ping', 'PING'),
    ('pxg', 'PXG'),
    ('scotty cameron', 'Scotty Cameron'),
    ('srixon', 'Srixon'),
    ('taylorMade', 'TaylorMade'),
    ('titleist', 'Titleist'),
    ('wilson staff', 'Wilson Staff'),

)

TAG_CHOICES = (

    ('sale', 'Sale'),

)


class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    listed_date = models.DateTimeField(auto_now_add=True)
    initial_quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='balls')
    manufacturer = models.CharField(max_length=25, choices=MANUFACTURER_CHOICES, blank=True, null=True, default='aldila')
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=25, choices=TAG_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    def __unicode__(self):
        return self.title
