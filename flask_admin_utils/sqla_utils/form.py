
from flask_admin.model.form import converts
from flask_admin.contrib.sqla.form import AdminModelConverter as Converter

try:
    from flask_admin_utils.sqla_utils.types import datetime
except ImportError:
    datetime = None
try:
    from flask_admin_utils.sqla_utils.types import password
except ImportError:
    password = None
try:
    from flask_admin_utils.sqla_utils.types import choice
except ImportError:
    choice = None
try:
    from flask_admin_utils.sqla_utils.types import color
except ImportError:
    color = None


class AdminModelConverter(Converter):
    """Flask-admin type converter for
    * arrow (Datetime)
    * password
    * choicetype
    * colour
    """

    @converts("ChoiceType")
    def convert_choice_type(self, field_args, **extra):
        field_args['choices'] = extra['column'].type.choices
        field_args['coerce'] = extra['column'].type.impl.python_type
        return choice.field(**field_args)

    @converts("PasswordType")
    def convert_password(self, field_args, **extra):
        return password.field(**field_args)

    @converts("ArrowType")
    def convert_arrow(self, field_args, **extra):
        return datetime.field(**field_args)

    @converts("ColorType")
    def convert_color(self, field_args, **extra):
        return color.field(**field_args)
