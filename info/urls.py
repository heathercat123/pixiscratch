from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.base, name="help"),
    path('scratch-alpha-help/', views.alpha_help, name="alpha_help"),
    re_path('studio/tips/(?P<tip>.+)', views.tips, name="tips"),  # This should only work for /help not /info
]
