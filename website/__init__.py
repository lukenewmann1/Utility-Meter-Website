import flask_login
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import login_manager
import csv
import os
from datetime import datetime

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.secret_key = 'admin'
    app.config['SECURITY_KEY'] = 'cookies password'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    app.run(host='192.168.2.14', port=4000)
    create_database(app)

    login_manager = flask_login.LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        db.create_all(app=app)
        print('* Database created successfully!')

def hour(meterID):
    filename = ("C:\\meter_tmp\\"+(str(meterID)+".csv"))
    with open(filename, 'r') as csvfile:
        rows = csvfile.readlines()
        hour_list = []
        j = 0
        k = -1
        i = -2
        FMT = '%Y-%m-%d_%H:%M'
        hour_high = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-12-25_14:25', FMT)
        hour_low = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-12-25_14:35', FMT)
        while j < 24:
            while hour_low >= (datetime.strptime((rows[k].split(",", -1))[0], FMT)
                               - datetime.strptime((rows[i].split(",", -1))[0], FMT)) <= hour_high:
                try:
                    datetime.strptime((rows[i-1].split(",", -1))[0], FMT)
                except IndexError:
                    status = 3
                    return status
                else:
                    i = i-1
            tmp = float((rows[k].split(",", -1))[1]) - float((rows[i].split(",", -1))[1])
            tmp = ('%.2f' % tmp)
            hour_list.append(tmp)
            j = j+1
            k = i
        return hour_list

def day(meterID):
    filename = ("C:\\meter_tmp\\"+(str(meterID)+".csv"))
    with open(filename, 'r') as csvfile:
        rows = csvfile.readlines()
        day_list = []
        j = 0
        k = -1
        i = -2
        FMT = '%Y-%m-%d_%H:%M'
        day_high = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-12-24_15:25', FMT)
        day_low = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-12-24_15:35', FMT)
        while j < 7:
            while day_low >= (datetime.strptime((rows[k].split(",", -1))[0], FMT) - datetime.strptime((rows[i].split(",", -1))[0], FMT)) <= day_high:
                try:
                    datetime.strptime((rows[i-1].split(",", -1))[0], FMT)
                except IndexError:
                    status = 3
                    return status
                else:
                    i = i-1
            tmp = float((rows[k].split(",", -1))[1]) - float((rows[i].split(",", -1))[1])
            tmp = ('%.2f' % tmp)
            day_list.append(tmp)
            j = j+1
            k = i
        return day_list

def month(meterID):
    filename = ("C:\\meter_tmp\\"+(str(meterID)+".csv"))
    with open(filename, 'r') as csvfile:
        rows = csvfile.readlines()
        month_list = []
        j = 0
        k = -1
        i = -2
        FMT = '%Y-%m-%d_%H:%M'
        month_high = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-11-25_15:25', FMT)
        month_low = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-11-25_15:35', FMT)
        while j < 12:
            while month_low >= (datetime.strptime((rows[k].split(",", -1))[0], FMT) - datetime.strptime((rows[i].split(",", -1))[0], FMT)) <= month_high:
                try:
                    datetime.strptime((rows[i-1].split(",", -1))[0], FMT)
                except IndexError:
                    status = 3
                    return status
                else:
                    i = i-1
            tmp = float((rows[k].split(",", -1))[1]) - float((rows[i].split(",", -1))[1])
            tmp = ('%.2f' % tmp)
            month_list.append(tmp)
            j = j+1
            k = i
        return month_list

def timestamp(meterID):
    filename = ("C:\\meter_tmp\\"+(str(meterID)+".csv"))
    with open(filename, 'r') as csvfile:
        rows = csvfile.readlines()
        t_stamp = str((rows[-1].split(",", -1))[0])
        return t_stamp

def meterType(meterID):
    filename = ("C:\\meter_tmp\\"+(str(meterID)+".csv"))
    with open(filename, 'r') as csvfile:
        rows = csvfile.readlines()
        try:
            type = str((rows[-1].split(",", -1))[2])
        except ValueError:
            type = 0
            return type
        return type

def axisHour(meterID):
    filename = ("C:\\meter_tmp\\"+(str(meterID)+".csv"))
    with open(filename, 'r') as csvfile:
        rows = csvfile.readlines()
        axis_list = []
        j = 0
        k = -1
        i = -2
        FMT = '%Y-%m-%d_%H:%M'
        hour_high = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-12-25_14:25', FMT)
        hour_low = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-12-25_14:35', FMT)
        while j < 24:
            while hour_low >= (datetime.strptime((rows[k].split(",", -1))[0], FMT) - datetime.strptime((rows[i].split(",", -1))[0], FMT)) <= hour_high:
                try:
                    datetime.strptime((rows[i-1].split(",", -1))[0], FMT)
                except IndexError:
                    status = 3
                    return status
                else:
                    i = i-1
            tmp = str(datetime.strptime(((rows[k].split(",", -1))[0]), FMT).strftime('%X'))
            axis_list.append(tmp)
            j = j+1
            k = i
        return axis_list

def axisWeek(meterID):
    filename = ("C:\\meter_tmp\\"+(str(meterID)+".csv"))
    with open(filename, 'r') as csvfile:
        rows = csvfile.readlines()
        axis_list = []
        j = 0
        k = -1
        i = -2
        FMT = '%Y-%m-%d_%H:%M'
        day_high = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-12-24_15:25', FMT)
        day_low = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-12-24_15:35', FMT)
        while j < 7:
            while day_low >= (datetime.strptime((rows[k].split(",", -1))[0], FMT) - datetime.strptime((rows[i].split(",", -1))[0], FMT)) <= day_high:
                try:
                    datetime.strptime((rows[i-1].split(",", -1))[0], FMT)
                except IndexError:
                    status = 3
                    return status
                else:
                    i = i-1
            tmp = str(datetime.strptime(((rows[k].split(",", -1))[0]), FMT).strftime('%a'))
            axis_list.append(tmp)
            j = j+1
            k = i
        return axis_list

def axisMonth(meterID):
    filename = ("C:\\meter_tmp\\"+(str(meterID)+".csv"))
    with open(filename, 'r') as csvfile:
        rows = csvfile.readlines()
        axis_list = []
        j = 0
        k = -1
        i = -2
        FMT = '%Y-%m-%d_%H:%M'
        month_high = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-11-25_15:25', FMT)
        month_low = datetime.strptime('2020-12-25_15:30', FMT) - datetime.strptime('2020-11-25_15:35', FMT)
        while j < 12:
            while month_low >= (datetime.strptime((rows[k].split(",", -1))[0], FMT) - datetime.strptime((rows[i].split(",", -1))[0], FMT)) <= month_high:
                try:
                    datetime.strptime((rows[i-1].split(",", -1))[0], FMT)
                except IndexError:
                    status = 3
                    return status
                else:
                    i = i-1
            tmp = str(datetime.strptime(((rows[k+20].split(",", -1))[0]), FMT).strftime('%b'))
            axis_list.append(tmp)
            j = j+1
            k = i
        return axis_list
# status 0 -> cannot find file in directory
# status 1 -> meter ID is not 0
# status 2 -> init. state
# status 3 -> insufficient data available
