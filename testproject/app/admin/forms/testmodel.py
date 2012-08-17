from django import forms

from app.models import TestModel

from redactorjs.widgets import AdminRedactorJS


class TestModelForm(forms.ModelForm):
    text = forms.CharField(
        widget=AdminRedactorJS
    )
    class Meta:
        model = TestModel
