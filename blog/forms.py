from django.forms import ModelForm

from .models import Post, Comment

from captcha.fields import ReCaptchaField


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'header_image', 'comments_enabled']
        exclude = ['user', 'created', 'edited']


class CommentForm(ModelForm):
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment', 'captcha']
        exclude = ['timestamp', 'post']
