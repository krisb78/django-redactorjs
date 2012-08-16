import os

from django.conf import settings


JS_URL = getattr(
    settings,
    'REDACTORJS_URL',
    os.path.join(
        os.path.join(
            settings.STATIC_URL,
            'redactor-js/js/redactor/redactor.js'
        )
    )
)
