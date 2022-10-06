from django.contrib import admin
from django.urls import path, re_path, include

from backend import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^jet/', include('jet.urls', 'jet')),
]
