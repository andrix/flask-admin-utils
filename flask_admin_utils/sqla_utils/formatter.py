# from colour import Color
from sqlalchemy_utils import Password

from flask.ext.admin.model import typefmt


def password_formatter(view, value):
    """
        Return "********" - if value is Password

        :param value:
            Value to check
    """
    return "*" * 8

#
# def colour_formatter(view, value):
#     return ""


BASE_FORMATTERS = typefmt.BASE_FORMATTERS.update({
    Password: password_formatter,
    # Color: colour_formatter,
})
