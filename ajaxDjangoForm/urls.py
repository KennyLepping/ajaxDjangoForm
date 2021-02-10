from django.contrib import admin
from django.urls import path, include
# from core import views as core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
]
