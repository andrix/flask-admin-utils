from wtforms import PasswordField


def password_formatter(view, value):
    """
        Return "********" - if value is Password

        :param value:
            Value to check
    """
    return "*" * 8


field = PasswordField
formatter = password_formatter