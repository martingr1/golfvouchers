from django.db import models
from django.utils import timezone


class Post(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    listed_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img")
    price = models.DecimalField(max_digits=6, decimal_places=0, null=False)

    def __unicode__(self):
        return self.title
