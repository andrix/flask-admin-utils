Flask-Admin-Utils
=================

This package provide a new view to support some types provided in the `sqlalchemy_utils` like
* Arrow (datetime)
* Password
* ChoiceType
* Colour type

Install
-------

```
pip install -e git+https://github.com/andrix/flask-admin-utils.git#egg=flask-admin-utils
```

Usage
-----

```python
from flask_admin_utils.sqla_utils import ModelView

# flask-admin code

admin = Admin(app, name='Example: SQLAlchemy')

# Add views
admin.add_view(ModelView(User, db.session))
...

```

Update May 21th, 2019: 
* make all the imports absolute
* update the requirements.txt with missing dependencies
