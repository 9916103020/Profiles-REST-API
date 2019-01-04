from django.contrib import admin

from . import models
"""From . means current location """

# Register your models here.
admin.site.register(models.UserProfile)
