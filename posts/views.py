# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post_view , Hashtag_view


from datetime import datetime
def bn(reguest):
    return HttpResponse('Hello! Its my project')
def bm(reguest):
    return HttpResponse(datetime.now)
def bi(reguest):
    return HttpResponse('Goodby user!')

def hashtag_view(reguest):
    if reguest.method == 'GET':
        hashtags = Hashtag_view.objects.all()
        data = {
            'hashtags': hashtags
        }
    return render(reguest, 'hashtag/hashtag.html' ,context=data)

def post_view(reguest):
    if reguest.method == 'GET':
        Posts = Post_view.objects.all()
        data = {
            'Posts': Posts
        }
    return render(reguest, 'post/postt.html' ,context=data)








