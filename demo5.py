#! /user/bin/env python
# -*- coding=UTF-8 -*-

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))  #返回文件的绝对路径
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
db = SQLAlchemy(app)  #db 对象是 SQLAlchemy 类的实例,表示程序使用的数据库


class Roles(db.Model):

    __tablename__ = "roles"

    id = db.Column(db.Integer,primary_key=True)  #id设为主键





if __name__ == '__main__':

    app.run(debug=True)