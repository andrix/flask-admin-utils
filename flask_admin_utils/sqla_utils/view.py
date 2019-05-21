from flask_admin.contrib.sqla import ModelView as MView

from flask_admin_utils.sqla_utils.form import AdminModelConverter
from flask_admin_utils.sqla_utils.types import BASE_FORMATTERS


class ModelView(MView):
    """New flask admin ModelView supporting new sqlalchemy types"""

    column_type_formatters = BASE_FORMATTERS
    model_form_converter = AdminModelConverter


class UserModelView(ModelView):
    """Handy link to define a UserModelView"""

    pass