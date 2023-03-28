from django.urls import path

from posts.views.base import IndexView, IndexRedirectView
from posts.views.comments import CommentDetailView
from posts.views.posts import PostDetail, PostCreateView



urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "product/", IndexRedirectView.as_view(), name="post_index_redirect"
    ),
    path("post/add", PostCreateView.as_view(), name="post_add"),
    path("post/<int:pk>", PostDetail.as_view(), name="post_detail"),
    path("review/<int:pk>", CommentDetailView.as_view(), name="comment_detail"),
]
