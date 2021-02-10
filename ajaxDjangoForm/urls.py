from django.contrib import admin
from django.urls import path
from core import views as core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core.contactPage), # FBV
    path('ajax/contact', core.postContact, name ='contact_submit'),
]
