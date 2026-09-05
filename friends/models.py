from django.db import models
from django.contrib.auth.models import User

class FriendRequest(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_friend_request"
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_friend_request"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sender", "receiver"],
                name="unique_friend_request"
            ),
            models.CheckConstraint(
                condition=~models.Q(sender=models.F("receiver")),
                name="friend_request_not_self"
            )
        ]


class Friendship(models.Model):
    user_a = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="friendship_as_a"
    )
    user_b = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="friendship_as_b"
    )
    created_at = models.DateTimeField(auto_now_add=True)