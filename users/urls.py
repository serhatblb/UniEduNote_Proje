# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Kayıt adresi
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
]