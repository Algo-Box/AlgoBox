from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'slug', 'content', 'status']