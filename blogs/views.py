from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from blogs.models import Blogs, Category, Comment


def post_by_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except:
        return redirect("home")
    posts = Blogs.objects.filter(status="published", category=category_id)
    context = {"posts": posts, "category": category}
    return render(request, "post_by_category.html", context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blogs, slug=slug, status="published")
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST["comment"]
        comment.save()
        return redirect(request.path_info)
    comments = Comment.objects.filter(blog=single_blog)
    comments_count = comments.count()
    context = {
        "single_blog": single_blog,
        "comments": comments,
        "comments_count": comments_count,
    }
    return render(request, "blogs.html", context)


def search(request):
    keywords = request.GET.get("keyword")
    print(keywords)
    blogs = Blogs.objects.filter(
        Q(title__icontains=keywords)
        | Q(short_description__icontains=keywords)
        | Q(blog_body__icontains=keywords),
        status="published",
    )

    context = {"blogs": blogs, "keyword": keywords}
    return render(request, "search.html", context)
