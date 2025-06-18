from django.contrib import admin
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from django.conf import settings as confsettings
from django.conf.urls.static import static

from scratchr2 import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.autodiscover()

urlpatterns = []
if settings.FORGOT_SETTINGS == 1:
    handler404 = 'scratchr2.views.forgot_settings_1'
    exit

if settings.FORGOT_SETTINGS == 2:
    handler404 = 'scratchr2.views.forgot_settings_2'
    exit

urlpatterns += [
    # Non-ScratchR2
    path('admin/', admin.site.urls),
    path('forgotsettings1/', views.forgot_settings_1),
    path('forgotsettings2/', views.forgot_settings_2),

    # Apps
    path('projects/', include("projects.urls")),
    path('news/', include("news.urls")),
    path('site-api/', include("siteapi.urls")),

    # Help
    path('help/', include("info.urls")),
    path('info/', include("info.urls")),

    # Users
    path('accounts/', include('accounts.urls')),
    path('users/', include("userprofiles.urls")),
    path('messages/', include("notifications.urls")),
    path('fragment/', include("fragment.urls")),
    path('mystuff/', include("mystuff.urls")),
    path('session/', views.session, name="session"),

    # Misc
    path('', views.homepage, name="home"),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('csrf_token/', views.csrf),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.STATIC_URL, document_root=confsettings.STATIC_ROOT)
