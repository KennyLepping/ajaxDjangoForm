from django.contrib import admin
from django.urls import path, include
# from core import views as core
from core2 import views as core2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),

    #app_2
    path('user', core2.userPanel),
    path('ajax/get_user_info', core2.getUserInfo, name = 'get_user_info'),
]
