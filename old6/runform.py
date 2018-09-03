#! /user/bin/env python
# -*- coding=UTF-8 -*-

from flask import Flask
from flask import render_template,session,redirect,url_for,flash
from flask.ext.wtf import FlaskForm  #进入Form表单
from flask.ext.bootstrap import Bootstrap  #一种开发木板

from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):

    name = StringField("what is you name",validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
bootstrap = Bootstrap(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form = form, name = session.get('name'))


if __name__ == '__main__':

    app.run(debug=True)