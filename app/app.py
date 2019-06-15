from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return show_the_login_form()
    else:
        return do_the_login()


@app.route('/logout')
def logout():
    return redirect('/')


@app.route('/book', methods=['GET','POST'])
def book():
    if request.method == 'GET':
        return show_booking_form()
    else:
        return do_the_booking()


@app.route('/bookings')
def bookings():
    return render_template('bookings.html')


def show_the_login_form():
    return render_template('login.html')


def do_the_login():
    return 'do the login'


def show_booking_form():
    return 'this is booking form'


def do_the_booking():
    return 'this is submitting booking form'


if __name__ == '__main__':

    app.config['DEBUG'] = True
    # db = SQLAlchemy()
    #
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bookameeting@localhost:5432'
    # db.init_app(app)

    app.run()
