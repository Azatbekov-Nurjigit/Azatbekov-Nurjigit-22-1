
from django.urls import path
from posts.views import bm,bi,bn,hashtag_view,post_view


urlpatterns = [
    path('hello/', bn),
    path('now_date/',bm),
    path('goodbye/',bi),
    path('posts/',hashtag_view),
    path('hashtags/',post_view),
]
