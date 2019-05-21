
from flask_admin.model import typefmt
from sqlalchemy_utils import Password

from flask_admin_utils.sqla_utils.types.color import formatter as color_formatter
from flask_admin_utils.sqla_utils.types.password import formatter as password_formatter

BASE_FORMATTERS = typefmt.BASE_FORMATTERS.update({Password: password_formatter})

try:
    from colour import Color
    BASE_FORMATTERS = typefmt.BASE_FORMATTERS.update({Color: color_formatter})
except ImportError:
    pass
