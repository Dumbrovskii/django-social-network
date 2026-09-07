from django.urls import path
from . import views


urlpatterns = [
    path("<str:username>", views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name='edit-profile'),
]