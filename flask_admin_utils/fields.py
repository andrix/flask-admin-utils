from widgets import ColorInput

from wtforms import StringField


class ColorField(StringField):
    widget = ColorInput()
