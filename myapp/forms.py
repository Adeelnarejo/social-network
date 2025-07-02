from django import forms
from .models import Post, OpenHouse

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control rounded',
                'rows': 3,
                'placeholder': "What's on your mind?"
            }),
        }



class OpenHouseForm(forms.ModelForm):
    class Meta:
        model = OpenHouse
        fields = '__all__'
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }