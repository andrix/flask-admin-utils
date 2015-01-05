from form import AdminModelConverter

from sqla_utils_types import BASE_FORMATTERS

from flask.ext.admin.contrib.sqla import ModelView as View


class ModelView(View):

    column_type_formatters = BASE_FORMATTERS

    model_form_converter = AdminModelConverter


class UserModelView(ModelView):
    pass