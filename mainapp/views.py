from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .form import EmailPostForm


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


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="published")
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # sending email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read" f"{post.title}"
            message = (
                f"Read {post.title} at {post.url}\n\n"
                f"{cd['name']}\s comments:{cd['commends']}"
            )

    else:
        form = EmailPostForm()
    context = {"post": post, "form": form}
    return render(request, "blog/share.html", context)
