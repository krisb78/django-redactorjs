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

        # Have to pass the name to build_attrs, otherwise it won't serialize!
        final_attrs = self.build_attrs(attrs, name=name)
        assert 'id' in final_attrs, "RedactorJS widget requires an id"

        html = [
            u'<textarea%s>%s</textarea>' % (
                flatatt(final_attrs),
                escape(value)
            )
        ]
        html.append(
            u'<script type="text/javascript">'
            u'$(document).ready(function(){$(%s).redactor();});'
            u'</script>' % u"'#%s'" % final_attrs['id']
        )

        return mark_safe(u'\n'.join(html))

    def _media(self):
        css = {
            'all': (settings.CSS_URL,)
        }
        js = [
            settings.JQUERY_JS_URL,
            settings.JS_URL

        ]
        return forms.Media(
            css=css,
            js=js
        )
    media = property(_media)


class AdminRedactorJS(
    admin_widgets.AdminTextareaWidget,
    RedactorJS
):
    """
    RedactorJS widget for the admin.
    """
    def render(self, name, value, attrs=None):
        html = super(
            AdminRedactorJS,
            self
        ).render(name, value, attrs=attrs)

        # setting clear to both makes sure that the label appears above
        # the widget.
        return mark_safe(
            u'<div style="clear: both;">%s</div>' % html
        )
