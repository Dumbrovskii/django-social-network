from friends.models import FriendRequest, Friendship
from django.db.models import Q

def get_friend_status(current_user, profile_user):
    incoming_friend_request = FriendRequest.objects.filter(
        sender=profile_user,
        receiver=current_user
    ).first()

    outcoming_friend_request = FriendRequest.objects.filter(
        sender=current_user,
        receiver=profile_user
    ).first()

    friendship = Friendship.objects.filter(
        Q(user_a=current_user, user_b=profile_user) |
        Q(user_a=profile_user, user_b=current_user)
    ).first()

    return {
        "profile_user": profile_user,
        "incoming_friend_request": incoming_friend_request,
        "outcoming_friend_request": outcoming_friend_request,
        "friendship": friendship,
    }