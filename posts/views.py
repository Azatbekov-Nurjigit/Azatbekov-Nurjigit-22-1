# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post, Hashtag, Comment
from posts.forms import PostCreateForm, CommentCreateForm
from datetime import datetime
from users.utils import get_user_from_request


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
            'hashtags': hashtags,
            'user': get_user_from_request(reguest)
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
            'Posts': posts,
            'user': get_user_from_request(reguest)
        }
        return render(reguest, 'post/postt.html', context=data)


def post_detail_view(reguest, **kwargs):
    if reguest.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        data = {
            'post': post,
            'comments': Comment.objects.filter(post=post),
            'form': CommentCreateForm,
            'user': get_user_from_request(reguest)
        }
        return render(reguest, 'yuiiu/vgjk.html', context=data)

    if reguest.method == 'POST':
        form = CommentCreateForm(data=reguest.POST)

        if form.is_valid():
            Comment.objects.create(
                author=reguest.user,
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            return redirect(f'/posts/{kwargs["id"]}/')
        else:
            post = Post.objects.get(id=kwargs['id'])
            comment = Comment.objects.filter(post=post)

            data = {
                'post': post,
                'comments': comment,
                'form': form,
                'user': get_user_from_request(reguest)
            }
            return render(reguest, 'yuiiu/vgjk.html', context=data)


def post_create_view(reguest):
    if reguest.method == 'GET':
        data = {
            'form': PostCreateForm,
            'user': get_user_from_request(reguest)
        }
        return render(reguest, 'post/create.html', context=data)

    if reguest.method == 'POST':
        form = PostCreateForm(data=reguest.POST)

        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/posts/')
        else:
            data = {
                'form': form,
                'user': get_user_from_request(reguest)
            }
            return render(reguest, 'post/create.html', context=data)
