from django import forms
from .models import MyModel

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = "__all__"