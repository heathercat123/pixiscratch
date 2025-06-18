from django.urls import path
from . import views

urlpatterns = [
    path('modal-registration/', views.modal_registration, name="modal-registration"),
    path('check_username/<str:username>/', views.check_username, name="check_username"),
    path('logout/', views.modal_registration, name="logout"),  # stub
    path('email_resend/', views.verify_email_popup, name="verify_email_popup"),
]
