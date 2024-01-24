from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Category, Blogs
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from .forms import CategoryForm, AddBlogForm


@login_required(login_url="login")
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blogs.objects.all().count()
    context = {"category_count": category_count, "blog_count": blog_count}
    return render(request, "dashboard/dashboard.html", context)


def categories(request):
    return render(request, "dashboard/categories.html")


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm()
    context = {
        "form": form,
    }
    return render(request, "dashboard/add_category.html", context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    print("Category")
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm(instance=category)
    context = {"form": form, "category": category}
    return render(request, "dashboard/edit_category.html", context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("categories")


def posts(request):
    posts = Blogs.objects.all()
    context = {"posts": posts}
    return render(request, "dashboard/posts.html", context)


def add_post(request):
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  ##? temporarily saving the form
            post.author = request.user
            post.save()
            title = form.cleaned_data["title"]
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect("posts")
        else:
            print(form.errors)
    form = AddBlogForm()
    context = {"form": form}
    return render(request, "dashboard/add_post.html", context)


def edit_post(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)  ##? temporarily saving
            title = form.cleaned_data["title"]
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect("posts")
    form = AddBlogForm(instance=post)
    context = {"form": form, "post": post}
    return render(request, "dashboard/edit_post.html", context)


def delete_post(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    return redirect("posts")
