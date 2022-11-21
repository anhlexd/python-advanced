from django import forms
from .models import Post

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content', 'image', 'status')