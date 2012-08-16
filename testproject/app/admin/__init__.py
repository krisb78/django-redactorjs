from django.contrib import admin

from .testmodel import TestModelAdmin

from app.models import TestModel


admin.site.register(
    TestModel,
    TestModelAdmin
)
