from django import forms
from .models import Post

class Postedit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']