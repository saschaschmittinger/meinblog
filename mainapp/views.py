from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


class PostView(generic.ListView):
    template_name = "blog/index.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 3


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(request, "blog/detail_view.html", {"post": post})
