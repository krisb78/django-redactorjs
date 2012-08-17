from django.db import models

from django.contrib import admin

from redactorjs.widgets import AdminRedactorJS


class TestModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': AdminRedactorJS
        }
    }
