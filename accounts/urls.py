from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^modal-registration/$', views.modal_registration, name="modal-registration"),
    url(r'^check_username/(?P<username>.+)/$', views.check_username, name="check_username"),
    url(r'^logout/$', views.modal_registration, name="logout"),  # stub
    url(r'^email_resend/$', views.verify_email_popup, name="verify_email_popup"),
]
