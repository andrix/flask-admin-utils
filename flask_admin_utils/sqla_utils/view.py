from sqlalchemy_utils import Password

from form import AdminModelConverter

from flask.ext.admin.model import typefmt
from flask.ext.admin.contrib.sqla import ModelView as View


def password_formatter(view, value):
    """
        Return "********" - if value is Password

        :param value:
            Value to check
    """
    return "*" * 8


BASE_FORMATTERS = typefmt.BASE_FORMATTERS.update({
    Password: password_formatter
})


class ModelView(View):

    column_type_formatters = BASE_FORMATTERS

    model_form_converter = AdminModelConverter


class UserModelView(ModelView):
    pass