from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blogs, Category


def home(request):
    featured_posts = Blogs.objects.filter(is_featured=True, status="published").order_by("updated_at")
    posts = Blogs.objects.filter(is_featured=False, status="published")
    context = {"featured_posts": featured_posts, "posts": posts}
    return render(request, "home.html", context)
