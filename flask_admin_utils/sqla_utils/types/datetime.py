import datetime
from dateutil import tz

from flask_admin.form.fields import DateTimeField


class NewDateTimeField(DateTimeField):
    def process_formdata(self, valuelist):
        if valuelist:
            date_str = ' '.join(valuelist)
            try:
                self.data = datetime.datetime.strptime(date_str, self.format).replace(tzinfo=tz.tzutc())
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid datetime value'))

field = NewDateTimeField