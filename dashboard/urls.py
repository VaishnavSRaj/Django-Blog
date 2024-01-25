from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    ##? CATEGORY CRUD
    path("categories", views.categories, name="categories"),
    path("add_category", views.add_category, name="add_category"),
    path("edit_category/<int:pk>/", views.edit_category, name="edit_category"),
    path("delete_category/<int:pk>/", views.delete_category, name="delete_category"),
    ##? POSTS CRUD
    path("posts/", views.posts, name="posts"),
    path("posts/add/", views.add_post, name="add_post"),
    path("posts/edit/<int:pk>/", views.edit_post, name="edit_post"),
    path("posts/delete/<int:pk>/", views.delete_post, name="delete_post"),
    ##? USERS CRUD
    path("users/", views.users, name="users"),
    path("users/add", views.add_users, name="add_users"),
    path("users/edit/<int:pk>/", views.edit_users, name="edit_users"),
    path("users/delete/<int:pk>/", views.delete_user, name="delete_user"),
]
