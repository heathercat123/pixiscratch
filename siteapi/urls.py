from django.urls import path
from . import views


urlpatterns = [
    path('comments/user/<str:username>/', views.usercomments, name="usercomments"),
    path('comments/with-deleted/user/<str:username>/', views.usercomments, name="usercomments-withdeleted"),
]
