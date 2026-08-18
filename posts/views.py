from django.db.models import Model
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

    return redirect("home")