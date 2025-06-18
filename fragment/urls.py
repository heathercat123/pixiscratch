from django.urls import path
from . import views

urlpatterns = [
    path('account-nav.json', views.account_nav, name="account_nav"),
]