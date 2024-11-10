
from django.contrib import admin
from django.urls import path,include
from auth_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_app/', include('auth_app.urls')),
    path('movies/', include('movies.urls')),
]
