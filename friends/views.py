from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FriendRequest, Friendship
from .services import get_friend_status
from django.db.models import Q


@login_required
def send_friend_request(request, user_id):
    receiver = get_object_or_404(User, id=user_id)

    if receiver == request.user:
        return HttpResponse(status=400)

    if FriendRequest.objects.filter(
        sender=request.user,
        receiver=receiver
    ).exists():
        return render(
            request,
            "friends/partials/friend_actions.html",
            get_friend_status(request.user, receiver),
        )

    if Friendship.objects.filter(
        Q(user_a=request.user, user_b=receiver) |
        Q(user_a=receiver, user_b=request.user)
    ).exists():
        return render(
            request,
            "friends/partials/friend_actions.html",
            get_friend_status(request.user, receiver),
        )

    FriendRequest.objects.create(
        sender=request.user,
        receiver=receiver,
    )

    return render(
        request,
        "friends/partials/friend_actions.html",
        get_friend_status(request.user, receiver)
    )


@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest,
        id=request_id,
        receiver=request.user,
    )

    profile_user = friend_request.sender

    Friendship.objects.create(
        user_a=friend_request.sender,
        user_b=friend_request.receiver
    )

    friend_request.delete()

    return render(
        request,
        "friends/partials/friend_actions.html",
        get_friend_status(request.user, profile_user)
    )

@login_required
def reject_friend_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest,
        id=request_id,
        receiver=request.user,
    )

    profile_user = friend_request.sender

    friend_request.delete()

    return render(
        request,
        "friends/partials/friend_actions.html",
        get_friend_status(request.user, profile_user)
    )