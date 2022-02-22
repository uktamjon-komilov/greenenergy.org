from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
)

urlpatterns += [

]


if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [
        path("rosetta/", include("rosetta.urls"))
    ]