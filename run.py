from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yoursecretkey'


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('Username required!'), Length(min=5, max=25,message='Username must be in 5 to 25 characters')])
    password = PasswordField('Password', validators=[InputRequired('Password required')],message='Un mot de pass long')
    submit = SubmitField('Submit')


@app.route('/Signup', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return f'<h1>Hi {form.username.data}!!. Your form is submitted successfully!!</h1>'

    return render_template('base.html', form=form)


