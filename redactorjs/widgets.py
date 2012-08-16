from django import forms

from django.contrib.admin import widgets as admin_widgets

from django.utils.html import escape

from django.forms.widgets import flatatt

from django.utils.safestring import mark_safe

try:
    from django.utils.encoding import smart_unicode
except ImportError:
    from django.forms.util import smart_unicode

from redactorjs import settings


class RedactorJS(forms.Textarea):
    """
    RedactorJS widget.
    """

    def render(self, name, value, attrs=None):
        value = value or ''
        value = smart_unicode(value)
        final_attrs = self.build_attrs(attrs)
        assert 'id' in final_attrs, "RedactorJS widget requires an id"

        html = [
            u'<textarea%s>%s</textarea>' % (
                flatatt(final_attrs),
                escape(value)
            )
        ]
        html.append(
            u'<script type="text/javascript"></script>'
        )

        return mark_safe(u'\n'.join(html))

    def _media(self):
        js = [settings.JS_URL]
        return forms.Media(js=js)
    media = property(_media)


class AdminRedactorJS(
    admin_widgets.AdminTextareaWidget,
    RedactorJS
):
    """
    RedactorJS widget for the admin.
    """
