from .models import Category, Tag, Post

def sidebar_data(request):
    return {
        "all_categories": Category.objects.all(),
        "all_tags": Tag.objects.all(),
        "recent_posts": Post.objects.filter(is_published=True).order_by("-created_at")[:5],
    }
