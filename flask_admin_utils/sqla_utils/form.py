from flask.ext.admin.model.form import converts
from flask.ext.admin.contrib.sqla.form import AdminModelConverter as Converter

from sqla_utils_types import arrow_type, password_type, choice_type, color_type


class AdminModelConverter(Converter):
    @converts("ChoiceType")
    def convert_choice_type(self, field_args, **extra):
        field_args['choices'] = extra['column'].type.choices
        field_args['coerce'] = extra['column'].type.impl.python_type
        return choice_type.field(**field_args)

    @converts("PasswordType")
    def convert_password(self, field_args, **extra):
        return password_type.field(**field_args)

    @converts("ArrowType")
    def convert_arrow(self, field_args, **extra):
        return arrow_type.field(**field_args)

    @converts("ColorType")
    def convert_color(self, field_args, **extra):
        return color_type.field(**field_args)
