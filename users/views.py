from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from friends.services import get_friend_status
from .forms import ProfileForm


@login_required(login_url="home")
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', kwargs={'username': request.user.username}))
    else:
        form = ProfileForm(instance=profile)

    return render(request, "users/edit_profile.html", {"form": form})


@login_required(login_url="home")
def profile(request, username):
    user = get_object_or_404(User, username=username)
    print(get_friend_status(request.user, user))
    print('get_friend_status(request.user, user)')

    return render(
        request,
        "users/profile.html",
        get_friend_status(request.user, user)
    )
