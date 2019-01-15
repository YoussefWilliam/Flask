from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegisterationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(),Length(min=2,max=20)])

    emai = StringField('Email',
                        validators=[DataRequired(),Email()])

    password = PasswordField('Password',
                              validators=[DataRequired()])

    confirmPassword= PasswordField('Confirm Password',
                                    validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign Up!')

class LoginForm(FlaskForm):
    emai = StringField('Email',
                        validators=[DataRequired(),Email()])

    password = PasswordField('Password',
                              validators=[DataRequired()])
    
    rememberMe = BooleanField('Remember Me')

    login = SubmitField('Sign In!')