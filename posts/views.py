# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post, Hashtag, Comment

from datetime import datetime

def bn(reguest):
    return HttpResponse('Hello! Its my project')


def bm(reguest):
    return HttpResponse(datetime.now)


def bi(reguest):
    return HttpResponse('Goodby user!')


def hashtag_view(reguest):
    if reguest.method == 'GET':
        hashtags = Hashtag.objects.all()
        data = {
            'hashtags': hashtags
        }
        return render(reguest, 'hashtag/hashtag.html', context=data)


def post_view(reguest):
    if reguest.method == 'GET':
        hashtag_id = reguest.GET.get('hashtag_id')
        if hashtag_id:
            posts = Hashtag.objects.get(id=hashtag_id).posts.all()
        else:
            posts = Post.objects.all()
        data = {
            'Posts': posts
        }
        return render(reguest, 'post/postt.html', context=data)


def post_detail_view(reguest, **kwargs):

    if reguest.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        data = {
            'post': post,
            'comments': Comment.objects.filter(post=post)
        }
        return render(reguest, 'yuiiu/vgjk.html', context=data)


