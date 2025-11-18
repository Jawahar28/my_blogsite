from django.urls import path
from . import views
from .views import CategoryPostListView, TagPostListView, SearchView, SavedPostsView, ProfileView

app_name = "blog"

urlpatterns = [
    # View Post
    path("", views.PostListView.as_view(), name="post-list"),

    # Search URL
    path("search/", SearchView.as_view(), name="search"),

    # Create, Edit, Delete Post
    path("create/", views.CreatePostView.as_view(), name="post-create"),
    path("<slug:slug>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path("<slug:slug>/delete/", views.PostDeleteView.as_view(), name="post-delete"),

    # Category and Tags URL
    path("category/<slug:slug>/", CategoryPostListView.as_view(), name="category-posts"),
    path("tag/<slug:slug>/", TagPostListView.as_view(), name="tag-posts"),
    
    # Catching slug at last
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post-detail"),
    
    #Bookmarks
    path("bookmark/", views.toggle_bookmark, name="toggle-bookmark"),
    path("saved/", SavedPostsView.as_view(), name="saved-posts"),

    # Profile View
    path("profile/<str:username>/", views.ProfileView.as_view(), name="profile"),

]
