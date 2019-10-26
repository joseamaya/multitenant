from django.contrib import admin

# Register your models here.
from shared.models import Client, Language

admin.site.register(Client)
admin.site.register(Language)