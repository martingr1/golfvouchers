from django import forms
from .models import Post


class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title', 'content', 'manufacturer', 'category', 'image', 'price', 'initial_quantity', 'tag')
        