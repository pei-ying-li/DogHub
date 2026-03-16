
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("apps.users.urls")),
    path("api/dogs/", include("apps.dogs.urls")),
    path("api/parks/", include("apps.parks.urls")),
]
