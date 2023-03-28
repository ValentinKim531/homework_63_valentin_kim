from django.views.generic import DetailView

from posts.models import Comment


class CommentDetailView(DetailView):
    template_name = "comment.html"
    model = Comment


