from django.contrib import admin
from django.urls import path, include
# from core import views as core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),

    # CBV
    # path('contact_cbv', core.ContactAjax.as_view(), name='contact_submit_cbv'),
]
