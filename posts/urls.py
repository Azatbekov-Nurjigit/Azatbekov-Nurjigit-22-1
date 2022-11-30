from django.urls import path
from posts.views import bm, bi, bn, hashtag_view, post_view, post_detail_view


urlpatterns = [
    path('hello/', bn),
    path('now_date/', bm),
    path('goodbye/', bi),
    path('hashtags/', hashtag_view),
    path('posts/', post_view),
    path('posts/<int:id>/', post_detail_view)

]
