from django import forms
from posts.models import Comment



class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=255)
    rate = forms.DecimalField(max_digits=10, decimal_places=1)


class CommentCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')