from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

# import only. register each files and
from .order import OrderAdmin

app_models = apps.get_app_config("order").get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
