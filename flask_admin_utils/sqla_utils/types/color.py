from jinja2 import Markup
from colour import Color
from wtforms import StringField, widgets


class ColorInput(widgets.Input):
    input_type = 'color'


class ColorField(StringField):
    widget = ColorInput()

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = Color(valuelist[0])
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid color value'))


def color_formatter(view, value):
    return Markup('<div style="float: left; margin: 2px -px 0 0; width: 15px; height: 15px; background: {0}"></div><div style="float: right">{0}</div>'.format(value))


field = ColorField
formatter = color_formatter
