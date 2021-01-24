from django.urls import path
from . import views
# from .webhooks import webhook

urlpatterns = [
    path('profile', views.profile, name='profile'),
    ]