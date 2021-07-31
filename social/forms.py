from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 4,
        'placeholder': 'Say something ...'
    }))

    class Meta:
        model = Post
        fields = ['body']
