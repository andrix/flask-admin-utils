from sqlalchemy_utils import Choice

from flask.ext.admin.form.fields import Select2Field


class SelectField(Select2Field):
    def process_data(self, value):
        if value is None:
            self.data = None
        else:
            try:
                if isinstance(value, Choice):
                    self.data = self.coerce(value.code)
                else:
                    self.data = self.coerce(value)
            except (ValueError, TypeError):
                self.data = None


field = SelectField
formatter = None