from django.db import models


class TestModel(models.Model):
    text = models.TextField(
        null=True,
        blank=True
    )
