from django.urls import re_path
from . import views


userregex = '[a-z|A-Z|0-9|-|_]+'
urlpatterns = [
    re_path(r'^(?P<username>' + userregex + ')/$', views.profile_detail, name="profile_detail"),
    re_path(r'^' + userregex + '/scratcher-promotion/$', views.scratcher_promotion_modal, name="scratcher_promotion_modal"),
]
