from django.contrib import admin
from .models import Contact
from django.apps import apps

'''
Dynamically register models from core app
See https://stackoverflow.com/questions/9443863/register-every-table-class-from-an-app-in-the-django-admin-page
'''

app = apps.get_app_config('core')

for model_name, model in app.models.items():
    admin.site.register(model)