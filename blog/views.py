from django.shortcuts import render
from django.utils import timezone
from blog.models import Post, Author
from django.contrib.auth import get_user_model


def author_details(author: Author) -> str:
    if not isinstance(author, get_user_model()):
        return str()

    return (
        f"{author.first_name} {author.last_name}".strip()
        or author.username
    )


def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})
