from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        upload_to='profile_photos',
        blank=True,
        null=True
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)