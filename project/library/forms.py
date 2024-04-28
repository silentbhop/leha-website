from .models import MediaFiles
from django.forms import ModelForm, TextInput, ClearableFileInput

class MediaFilesForm(ModelForm):
    class Meta:
        model = MediaFiles
        fields = ['title', 'file']

        widgets = {
            'title' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
            'file' : ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }