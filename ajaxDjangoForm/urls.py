from django.contrib import admin
from django.urls import path, include
# from core import views as core
from core2 import views as core2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    
    path('core2', core2.UserInfo.as_view(), name = 'get_user_info')
]
