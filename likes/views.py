from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Like
from blog.models import Post

# Create your views here.

@login_required
def toggle_like(request):
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()
        status = "unliked"
    else:
        status = "liked"

    return JsonResponse({
        "status": status,
        "likes_count": post.likes.count()
    })


