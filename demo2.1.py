#! /user/bin/env python
# -*- coding=UTF-8 -*-

from flask import Flask
from flask import request,make_response,redirect,abort


app = Flask(__name__)


@app.route("/")
def index():

    return "<h1>Hello world!</h1>"


@app.route("/user/<name>")
def user(name):

    return "<h1>hello {}</h1>".format(name)



@app.route("/ua")
def ua():

    return "<p>请求的User-Agent:{}</p>".format(request.headers.get("User-Agent"))

@app.route("/badreq")
def badreq():

    return '<h1>Bad Request!</h1>',404

@app.route("/makeres")
def makeres():

    response = make_response("<h1>response set cookie!</h1>")
    response.set_cookie("key","hsakdhakj")

    return response


@app.route("/red")
def red():

    return redirect("ua")

@app.route("/users/<id>")
def get_user(id):
    if id:
        return '<p>user id is:{}</p>'.format(id)

    return abort(404)



if __name__ == '__main__':

    app.run(debug=True)