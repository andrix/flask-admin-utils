import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_utils import ChoiceType, PasswordType

from flask.ext.admin import Admin

from flask_admin_utils.sqla_utils import ModelView


# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['DATABASE_FILE'] = 'test.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

USERS_TYPE = (
    ("1", "Active"),
    ("0", "Not Active"),
)


# Create models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(PasswordType(schemes=['md5_crypt']))
    status = db.Column(ChoiceType(choices=USERS_TYPE), default="1")

    # Required for administrative interface. For python 3 please use __str__ instead.
    def __unicode__(self):
        return self.username


# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


# Customized User model admin
class UserAdmin(ModelView):
    pass

# Create admin
admin = Admin(app, name='Example: SQLAlchemy')

# Add views
admin.add_view(UserAdmin(User, db.session))


def build_sample_db():
    """
    Populate a small db with some example entries.
    """

    import random

    db.drop_all()
    db.create_all()

    # Create sample Users
    first_names = [
        'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie', 'Sophie', 'Mia',
        'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
        'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
    ]
    last_names = [
        'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
        'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
        'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
    ]

    for i in range(len(first_names)):
        user = User()
        user.first_name = first_names[i]
        user.username = first_names[i].lower()
        user.last_name = last_names[i]
        user.email = user.username + "@example.com"
        user.password = str(random.randint(0, 100000))
        db.session.add(user)

    db.session.commit()
    return

if __name__ == '__main__':
    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    # Start app
    app.run(debug=True)