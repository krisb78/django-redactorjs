import os

from django.conf import settings


JS_URL = getattr(
    settings,
    'REDACTORJS_URL',
    os.path.join(
        settings.STATIC_URL,
        'redactor-js/js/redactor/redactor.js'
    )
)

CSS_URL = getattr(
    settings,
    'REDACTORJS_CSS_URL',
    os.path.join(
        settings.STATIC_URL,
        'redactor-js/js/redactor/css/redactor.css'
    )
)

JQUERY_JS_URL = getattr(
    settings,
    'JQUERY_JS_URL',
    os.path.join(
        settings.STATIC_URL,
        'redactor-js/js/jquery-1.7.min.js'
    )
)
