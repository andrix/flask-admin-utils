from form import AdminModelConverter

from formatter import BASE_FORMATTERS

from flask.ext.admin.contrib.sqla import ModelView as View


class ModelView(View):

    column_type_formatters = BASE_FORMATTERS

    model_form_converter = AdminModelConverter


class UserModelView(ModelView):
    pass