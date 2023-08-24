from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
schema_view = get_schema_view(
    openapi.Info(
        title="Spotify API",
        description="...",
        default_version="v2",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui("swagger")),
    path('account/', include('user_account.urls')),
    path('', include('songs.urls')),
    path('review/', include('review.urls')),
    path('', include('playlists.urls')),
    path('accounts/', include('allauth.urls')),
    path('favorite/', include('libraries.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
]
urlpatterns += staticfiles_urlpatterns()
