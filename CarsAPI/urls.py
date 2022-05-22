from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('CarsAPI.web.urls')),
    path('api/', include('CarsAPI.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('CarsAPI.authentication.urls')),
)
