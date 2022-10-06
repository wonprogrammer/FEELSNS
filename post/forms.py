from django import forms
from .models import Post, Comment

class Postedit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']
