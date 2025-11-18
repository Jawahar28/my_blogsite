from django.shortcuts import render,redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from blog.models import Post
from .models import Comment


# Create your views here.

@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get("content")
        parent_id = request.POST.get("parent_id")

        parent = Comment.objects.get(id=parent_id) if parent_id else None

        Comment.objects.create(
            user=request.user,
            post=post,
            content=content,
            parent=parent
        )

    return redirect("blog:post-detail", slug=post.slug)

