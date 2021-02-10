from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
	#CBV
    path('', views.ContactAjax.as_view(), name='contact_submit_cbv'),
]