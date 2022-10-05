from django.forms import ModelForm
from .models import UserModel

class FileUploadForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['nickname', 'bio', 'user_images']