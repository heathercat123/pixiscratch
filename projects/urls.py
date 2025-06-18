from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/editor/', views.editor),
    path('editor/', views.editor, name="editor"),
]
