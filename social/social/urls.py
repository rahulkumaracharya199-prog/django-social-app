from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from network.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("accounts/login/", login_view , name="login"),
    path("accounts/register/", register_view , name="register"),
    path("accounts/logout/", logout_view , name="logout"),
    # profile routes
    path("profile/", profileindex, name="profile"),
    path("createpost/", CreatePost, name="createpost")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
