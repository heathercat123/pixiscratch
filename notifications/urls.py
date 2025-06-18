from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications, name="notifications"),
    path('ajax/user-activity/', views.user_feed, name="user_feed"),
]
