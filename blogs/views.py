from django.http import HttpResponse
from django.shortcuts import redirect, render

from blogs.models import Blogs, Category


def post_by_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except:
        return redirect("home")
    posts = Blogs.objects.filter(status="published", category=category_id)
    context = {"posts": posts, "category": category}
    return render(request, "post_by_category.html", context)
