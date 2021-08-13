from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 4,
        'placeholder': 'Say something ...'
    }))

    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['body', 'image']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 4,
        'placeholder': 'Write your comment ...'
    }))

    class Meta:
        model = Comment
        fields = ['comment']
