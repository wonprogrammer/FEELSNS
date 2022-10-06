from django import forms
from .models import Post, Comment

class Postedit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post','nickname','comment']
