from django.contrib import admin

from .forms.testmodel import TestModelForm


class TestModelAdmin(admin.ModelAdmin):
    form = TestModelForm
