from django.forms import ModelForm
from django import forms
from .models import UserModel

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['nickname', 'bio', 'user_images']