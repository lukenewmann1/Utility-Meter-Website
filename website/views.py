from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import csv
import os
from datetime import datetime
from website import *
import time

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/consumption')
@login_required
def usage():
    usage_hour_1 = 0,
    usage_hour_2 = 0
    usage_hour_3 = 0
    usage_hour_4 = 0
    usage_day_1 = 0
    usage_day_2 = 0
    usage_day_3 = 0
    usage_day_4 = 0
    usage_week_1 = 0
    usage_week_2 = 0
    usage_week_3 = 0
    usage_week_4 = 0
    usage_month_1 = 0
    usage_month_2 = 0
    usage_month_3 = 0
    usage_month_4 = 0
    current_timestamp_1 = 0
    current_timestamp_2 = 0
    current_timestamp_3 = 0
    current_timestamp_4 = 0
    status_1 = 2
    status_2 = 2
    status_3 = 2
    status_4 = 2
    labels_hour_1 = 0
    values_hour_1 = 0
    labels_hour_2 = 0
    values_hour_2 = 0
    labels_hour_3 = 0
    values_hour_3 = 0
    labels_hour_4 = 0
    values_hour_4 = 0
    labels_week_1 = 0
    values_week_1 = 0
    labels_week_2 = 0
    values_week_2 = 0
    labels_week_3 = 0
    values_week_3 = 0
    labels_week_4 = 0
    values_week_4 = 0
    labels_month_1 = 0
    values_month_1 = 0
    labels_month_2 = 0
    values_month_2 = 0
    labels_month_3 = 0
    values_month_3 = 0
    labels_month_4 = 0
    values_month_4 = 0
    meter_type_1 = 0
    meter_type_2 = 0
    meter_type_3 = 0
    meter_type_4 = 0
    headings = ("Time Range","Usage Statistics")

    if current_user.meterID_1 != 0:
        status_1 = 1
        if not os.path.isfile("C:\\Users\\LukeNewman\\OneDrive - Queen's University\\Capstone\\Luke\\MeterIDs\\"+(str(current_user.meterID_1)+".csv")):
            status_1 = 0
        else:
            meterID_1_hour = hour(current_user.meterID_1)
            meterID_1_day = day(current_user.meterID_1)
            meterID_1_month = month(current_user.meterID_1)
            current_timestamp_1 = timestamp(current_user.meterID_1)
            meter_type_1 = int(meterType(current_user.meterID_1))

            if meter_type_1 == 12 or meter_type_1 == 156 or meter_type_1 == 11:
                meter_type_1 = "Gas"
            elif meter_type_1 == 13 or meter_type_1 == 203:
                meter_type_1 = "Water"
            elif meter_type_1 == 5:
                meter_type_1 = "Electricity"
            elif meter_type_1 == 0:
                meter_type_1 = "*Index Out of Range Error*"
            else:
                meter_type_1 = "Undefined"

            if meterID_1_hour != 3:
                usage_hour_1 = meterID_1_hour[0]
                data_hour = [(1,meterID_1_hour[23]),(2,meterID_1_hour[22]),(3,meterID_1_hour[21]),(4,meterID_1_hour[20]),
                             (5,meterID_1_hour[19]),(6,meterID_1_hour[18]),(7,meterID_1_hour[17]),(8,meterID_1_hour[16]),
                             (9,meterID_1_hour[15]),(10,meterID_1_hour[14]),(11,meterID_1_hour[13]),(12,meterID_1_hour[12]),
                             (13,meterID_1_hour[11]),(14,meterID_1_hour[10]),(15,meterID_1_hour[9]),(16,meterID_1_hour[8]),
                             (17,meterID_1_hour[7]),(18,meterID_1_hour[6]),(19,meterID_1_hour[5]),(20,meterID_1_hour[4]),
                             (21,meterID_1_hour[3]),(22,meterID_1_hour[2]),(23,meterID_1_hour[1]),(24,meterID_1_hour[0])]
                labels_hour_1 = [row[0] for row in data_hour]
                values_hour_1 = [row[1] for row in data_hour]
            else:
                usage_hour_1 = "{Insufficient Data}"
                null_data_hour = [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),
                                  (14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0),(24,0)]
                labels_hour_1 = [row[0] for row in null_data_hour]
                values_hour_1 = [row[1] for row in null_data_hour]

            if meterID_1_day != 3:
                usage_day_1 = meterID_1_day[0]
            else:
                usage_day_1 = "{Insufficient Data}"

            if meterID_1_day != 3:
                usage_week_1 = float(meterID_1_day[0]) + float(meterID_1_day[1]) + float(meterID_1_day[2]) + float(meterID_1_day[3]) + float(meterID_1_day[4]) + float(meterID_1_day[5]) + float(meterID_1_day[6])
                usage_week_1 = ('%.2f' % usage_week_1)
                data_week = [("Mon.",meterID_1_day[6]),("Tue.",meterID_1_day[5]),("Wed",meterID_1_day[4]),
                             ("Thu.",meterID_1_day[3]),("Fri.",meterID_1_day[2]),("Sat.",meterID_1_day[1]),
                             ("Sun.",meterID_1_day[0])]
                labels_week_1 = [row[0] for row in data_week]
                values_week_1 = [row[1] for row in data_week]
            else:
                usage_week_1 = "{Insufficient Data}"
                null_data_week = [("Mon.",0),("Tue.",0),("Wed",0),("Thu.",0),("Fri.",0),("Sat.",0),("Sun.",0)]
                labels_week_1 = [row[0] for row in null_data_week]
                values_week_1 = [row[1] for row in null_data_week]

            if meterID_1_month != 3:
                usage_month_1 = meterID_1_month[0]
                data_month = [("Jan.",meterID_1_month[11]),("Feb.",meterID_1_month[10]),("Mar.",meterID_1_month[9]),
                              ("Apr.",meterID_1_month[8]),("May.",meterID_1_month[7]),("Jun.",meterID_1_month[6]),
                              ("Jul",meterID_1_month[5]),("Aug.",meterID_1_month[4]),("Sep.",meterID_1_month[3]),
                              ("Oct.",meterID_1_month[2]),("Nov.",meterID_1_month[1]),("Dec.",meterID_1_month[0])]
                labels_month_1 = [row[0] for row in data_month]
                values_month_1 = [row[1] for row in data_month]
            else:
                usage_month_1 = "{Insufficient Data}"
                null_data_month = [("Jan.",0),("Feb.",0),("Mar.",0),("Apr.",0),("May.",0),("Jun.",0),("Jul",0),
                                   ("Aug.",0),("Sep.",0),("Oct.",0),("Nov.",0),("Dec.",0)]
                labels_month_1 = [row[0] for row in null_data_month]
                values_month_1 = [row[1] for row in null_data_month]

    if current_user.meterID_2 != 0:
        status_2 = 1
        if not os.path.isfile("C:\\Users\\LukeNewman\\OneDrive - Queen's University\\Capstone\\Luke\\MeterIDs\\"+(str(current_user.meterID_2)+".csv")):
            status_2 = 0
        else:
            meterID_2_hour = hour(current_user.meterID_2)
            meterID_2_day = day(current_user.meterID_2)
            meterID_2_month = month(current_user.meterID_2)
            current_timestamp_2 = timestamp(current_user.meterID_2)
            meter_type_2 = int(meterType(current_user.meterID_2))

            if meter_type_2 == 12 or meter_type_2 == 156 or meter_type_2 == 11:
                meter_type_2 = "Gas"
            elif meter_type_2 == 13 or meter_type_2 == 203:
                meter_type_2 = "Water"
            elif meter_type_2 == 5:
                meter_type_2 = "Electricity"
            elif meter_type_2 == 0:
                meter_type_2 = "*Index Out of Range Error*"
            else:
                meter_type_2 = "Undefined"

            if meterID_2_hour != 3:
                usage_hour_2 = meterID_2_hour[0]
                data_hour = [(1,meterID_2_hour[23]),(2,meterID_2_hour[22]),(3,meterID_2_hour[21]),(4,meterID_2_hour[20]),
                             (5,meterID_2_hour[19]),(6,meterID_2_hour[18]),(7,meterID_2_hour[17]),(8,meterID_2_hour[16]),
                             (9,meterID_2_hour[15]),(10,meterID_2_hour[14]),(11,meterID_2_hour[13]),(12,meterID_2_hour[12]),
                             (13,meterID_2_hour[11]),(14,meterID_2_hour[10]),(15,meterID_2_hour[9]),(16,meterID_2_hour[8]),
                             (17,meterID_2_hour[7]),(18,meterID_2_hour[6]),(19,meterID_2_hour[5]),(20,meterID_2_hour[4]),
                             (21,meterID_2_hour[3]),(22,meterID_2_hour[2]),(23,meterID_2_hour[1]),(24,meterID_2_hour[0])]
                labels_hour_2 = [row[0] for row in data_hour]
                values_hour_2 = [row[1] for row in data_hour]
            else:
                usage_hour_2 = "{Insufficient Data}"
                null_data_hour = [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),
                                  (14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0),(24,0)]
                labels_hour_2 = [row[0] for row in null_data_hour]
                values_hour_2 = [row[1] for row in null_data_hour]

            if meterID_2_day != 3:
                usage_day_2 = meterID_2_day[0]
            else:
                usage_day_2 = "{Insufficient Data}"

            if meterID_2_day != 3:
                usage_week_2 = float(meterID_2_day[0]) + float(meterID_2_day[1]) + float(meterID_2_day[2]) + float(meterID_2_day[3]) + float(meterID_2_day[4]) + float(meterID_2_day[5]) + float(meterID_2_day[6])
                usage_week_2 = ('%.2f' % usage_week_2)
                data_week = [("Mon.",meterID_2_day[6]),("Tue.",meterID_2_day[5]),("Wed",meterID_2_day[4]),
                             ("Thu.",meterID_2_day[3]),("Fri.",meterID_2_day[2]),("Sat.",meterID_2_day[1]),
                             ("Sun.",meterID_2_day[0])]
                labels_week_2 = [row[0] for row in data_week]
                values_week_2 = [row[1] for row in data_week]
            else:
                usage_week_2 = "{Insufficient Data}"
                null_data_week = [("Mon.",0),("Tue.",0),("Wed",0),("Thu.",0),("Fri.",0),("Sat.",0),("Sun.",0)]
                labels_week_2 = [row[0] for row in null_data_week]
                values_week_2 = [row[1] for row in null_data_week]

            if meterID_2_month != 3:
                usage_month_2 = meterID_2_month[0]
                data_month = [("Jan.",meterID_2_month[11]),("Feb.",meterID_2_month[10]),("Mar.",meterID_2_month[9]),
                              ("Apr.",meterID_2_month[8]),("May.",meterID_2_month[7]),("Jun.",meterID_2_month[6]),
                              ("Jul",meterID_2_month[5]),("Aug.",meterID_2_month[4]),("Sep.",meterID_2_month[3]),
                              ("Oct.",meterID_2_month[2]),("Nov.",meterID_2_month[1]),("Dec.",meterID_2_month[0])]
                labels_month_2 = [row[0] for row in data_month]
                values_month_2 = [row[1] for row in data_month]
            else:
                usage_month_2 = "{Insufficient Data}"
                null_data_month = [("Jan.",0),("Feb.",0),("Mar.",0),("Apr.",0),("May.",0),("Jun.",0),("Jul",0),
                                   ("Aug.",0),("Sep.",0),("Oct.",0),("Nov.",0),("Dec.",0)]
                labels_month_2 = [row[0] for row in null_data_month]
                values_month_2 = [row[1] for row in null_data_month]

    if current_user.meterID_3 != 0:
        status_3 = 1
        if not os.path.isfile("C:\\Users\\LukeNewman\\OneDrive - Queen's University\\Capstone\\Luke\\MeterIDs\\"+(str(current_user.meterID_3)+".csv")):
            status_3 = 0
        else:
            meterID_3_hour = hour(current_user.meterID_3)
            meterID_3_day = day(current_user.meterID_3)
            meterID_3_month = month(current_user.meterID_3)
            current_timestamp_3 = timestamp(current_user.meterID_3)
            meter_type_3 = int(meterType(current_user.meterID_3))

            if meter_type_3 == 12 or meter_type_3 == 156 or meter_type_3 == 11:
                meter_type_3 = "Gas"
            elif meter_type_3 == 13 or meter_type_3 == 203:
                meter_type_3 = "Water"
            elif meter_type_3 == 5:
                meter_type_3 = "Electricity"
            elif meter_type_3 == 0:
                meter_type_3 = "*Index Out of Range Error*"
            else:
                meter_type_3 = "Undefined"

            if meterID_3_hour != 3:
                usage_hour_3 = meterID_3_hour[0]
                data_hour = [(1,meterID_3_hour[23]),(2,meterID_3_hour[22]),(3,meterID_3_hour[21]),(4,meterID_3_hour[20]),
                             (5,meterID_3_hour[19]),(6,meterID_3_hour[18]),(7,meterID_3_hour[17]),(8,meterID_3_hour[16]),
                             (9,meterID_3_hour[15]),(10,meterID_3_hour[14]),(11,meterID_3_hour[13]),(12,meterID_3_hour[12]),
                             (13,meterID_3_hour[11]),(14,meterID_3_hour[10]),(15,meterID_3_hour[9]),(16,meterID_3_hour[8]),
                             (17,meterID_3_hour[7]),(18,meterID_3_hour[6]),(19,meterID_3_hour[5]),(20,meterID_3_hour[4]),
                             (21,meterID_3_hour[3]),(22,meterID_3_hour[2]),(23,meterID_3_hour[1]),(24,meterID_3_hour[0])]
                labels_hour_3 = [row[0] for row in data_hour]
                values_hour_3 = [row[1] for row in data_hour]
            else:
                usage_hour_3 = "{Insufficient Data}"
                null_data_hour = [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),
                                  (14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0),(24,0)]
                labels_hour_3 = [row[0] for row in null_data_hour]
                values_hour_3 = [row[1] for row in null_data_hour]

            if meterID_3_day != 3:
                usage_day_3 = meterID_3_day[0]
            else:
                usage_day_3 = "{Insufficient Data}"

            if meterID_3_day != 3:
                usage_week_3 = float(meterID_3_day[0]) + float(meterID_3_day[1]) + float(meterID_3_day[2]) + float(meterID_3_day[3]) + float(meterID_3_day[4]) + float(meterID_3_day[5]) + float(meterID_3_day[6])
                usage_week_3 = ('%.2f' % usage_week_3)
                data_week = [("Mon.",meterID_3_day[6]),("Tue.",meterID_3_day[5]),("Wed",meterID_3_day[4]),
                             ("Thu.",meterID_3_day[3]),("Fri.",meterID_3_day[2]),("Sat.",meterID_3_day[1]),
                             ("Sun.",meterID_3_day[0])]
                labels_week_3 = [row[0] for row in data_week]
                values_week_3 = [row[1] for row in data_week]
            else:
                usage_week_3 = "{Insufficient Data}"
                null_data_week = [("Mon.",0),("Tue.",0),("Wed",0),("Thu.",0),("Fri.",0),("Sat.",0),("Sun.",0)]
                labels_week_3 = [row[0] for row in null_data_week]
                values_week_3 = [row[1] for row in null_data_week]

            if meterID_3_month != 3:
                usage_month_3 = meterID_3_month[0]
                data_month = [("Jan.",meterID_3_month[11]),("Feb.",meterID_3_month[10]),("Mar.",meterID_3_month[9]),
                              ("Apr.",meterID_3_month[8]),("May.",meterID_3_month[7]),("Jun.",meterID_3_month[6]),
                              ("Jul",meterID_3_month[5]),("Aug.",meterID_3_month[4]),("Sep.",meterID_3_month[3]),
                              ("Oct.",meterID_3_month[2]),("Nov.",meterID_3_month[1]),("Dec.",meterID_3_month[0])]
                labels_month_3 = [row[0] for row in data_month]
                values_month_3 = [row[1] for row in data_month]
            else:
                usage_month_3 = "{Insufficient Data}"
                null_data_month = [("Jan.",0),("Feb.",0),("Mar.",0),("Apr.",0),("May.",0),("Jun.",0),("Jul",0),
                                   ("Aug.",0),("Sep.",0),("Oct.",0),("Nov.",0),("Dec.",0)]
                labels_month_3 = [row[0] for row in null_data_month]
                values_month_3 = [row[1] for row in null_data_month]

    if current_user.meterID_4 != 0:
        status_4 = 1
        if not os.path.isfile("C:\\Users\\LukeNewman\\OneDrive - Queen's University\\Capstone\\Luke\\MeterIDs\\"+(str(current_user.meterID_4)+".csv")):
            status_4 = 0
        else:
            meterID_4_hour = hour(current_user.meterID_4)
            meterID_4_day = day(current_user.meterID_4)
            meterID_4_month = month(current_user.meterID_4)
            current_timestamp_4 = timestamp(current_user.meterID_4)
            meter_type_4 = int(meterType(current_user.meterID_4))

            if meter_type_4 == 12 or meter_type_4 == 156 or meter_type_4 == 11:
                meter_type_4 = "Gas"
            elif meter_type_4 == 13 or meter_type_4 == 203:
                meter_type_4 = "Water"
            elif meter_type_4 == 5:
                meter_type_4 = "Electricity"
            elif meter_type_4 == 0:
                meter_type_4 = "*Index Out of Range Error*"
            else:
                meter_type_4 = "Undefined"

            if meterID_4_hour != 3:
                usage_hour_4 = meterID_4_hour[0]
                data_hour = [(1,meterID_4_hour[23]),(2,meterID_4_hour[22]),(3,meterID_4_hour[21]),(4,meterID_4_hour[20]),
                             (5,meterID_4_hour[19]),(6,meterID_4_hour[18]),(7,meterID_4_hour[17]),(8,meterID_4_hour[16]),
                             (9,meterID_4_hour[15]),(10,meterID_4_hour[14]),(11,meterID_4_hour[13]),(12,meterID_4_hour[12]),
                             (13,meterID_4_hour[11]),(14,meterID_4_hour[10]),(15,meterID_4_hour[9]),(16,meterID_4_hour[8]),
                             (17,meterID_4_hour[7]),(18,meterID_4_hour[6]),(19,meterID_4_hour[5]),(20,meterID_4_hour[4]),
                             (21,meterID_4_hour[3]),(22,meterID_4_hour[2]),(23,meterID_4_hour[1]),(24,meterID_4_hour[0])]
                labels_hour_4 = [row[0] for row in data_hour]
                values_hour_4 = [row[1] for row in data_hour]
            else:
                usage_hour_4 = "{Insufficient Data}"
                null_data_hour = [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),
                                  (14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0),(24,0)]
                labels_hour_4 = [row[0] for row in null_data_hour]
                values_hour_4 = [row[1] for row in null_data_hour]

            if meterID_4_day != 3:
                usage_day_4 = meterID_4_day[0]
            else:
                usage_day_4 = "{Insufficient Data}"

            if meterID_4_day != 3:
                usage_week_4 = float(meterID_4_day[0]) + float(meterID_4_day[1]) + float(meterID_4_day[2]) + float(meterID_4_day[3]) + float(meterID_4_day[4]) + float(meterID_4_day[5]) + float(meterID_4_day[6])
                usage_week_4 = ('%.2f' % usage_week_4)
                data_week = [("Mon.",meterID_4_day[6]),("Tue.",meterID_4_day[5]),("Wed",meterID_4_day[4]),
                             ("Thu.",meterID_4_day[3]),("Fri.",meterID_4_day[2]),("Sat.",meterID_4_day[1]),
                             ("Sun.",meterID_4_day[0])]
                labels_week_4 = [row[0] for row in data_week]
                values_week_4 = [row[1] for row in data_week]
            else:
                usage_week_4 = "{Insufficient Data}"
                null_data_week = [("Mon.",0),("Tue.",0),("Wed",0),("Thu.",0),("Fri.",0),("Sat.",0),("Sun.",0)]
                labels_week_4 = [row[0] for row in null_data_week]
                values_week_4 = [row[1] for row in null_data_week]

            if meterID_4_month != 3:
                usage_month_4 = meterID_4_month[0]
                data_month = [("Jan.",meterID_4_month[11]),("Feb.",meterID_4_month[10]),("Mar.",meterID_4_month[9]),
                              ("Apr.",meterID_4_month[8]),("May.",meterID_4_month[7]),("Jun.",meterID_4_month[6]),
                              ("Jul",meterID_4_month[5]),("Aug.",meterID_4_month[4]),("Sep.",meterID_4_month[3]),
                              ("Oct.",meterID_4_month[2]),("Nov.",meterID_4_month[1]),("Dec.",meterID_4_month[0])]
                labels_month_4 = [row[0] for row in data_month]
                values_month_4 = [row[1] for row in data_month]
            else:
                usage_month_4 = "{Insufficient Data}"
                null_data_month = [("Jan.",0),("Feb.",0),("Mar.",0),("Apr.",0),("May.",0),("Jun.",0),("Jul",0),
                                   ("Aug.",0),("Sep.",0),("Oct.",0),("Nov.",0),("Dec.",0)]
                labels_month_4 = [row[0] for row in null_data_month]
                values_month_4 = [row[1] for row in null_data_month]

    return render_template("consumption.html",
                           user=current_user,
                           first_name=current_user.first_name,
                           last_name=current_user.last_name,
                           meterId_1=current_user.meterID_1,
                           meterId_2=current_user.meterID_2,
                           meterId_3=current_user.meterID_3,
                           meterId_4=current_user.meterID_4,
                           headings=headings,
                           usage_hour=usage_hour_1,
                           usage_hour_2=usage_hour_2,
                           usage_hour_3=usage_hour_3,
                           usage_hour_4=usage_hour_4,
                           usage_day=usage_day_1,
                           usage_day_2=usage_day_2,
                           usage_day_3=usage_day_3,
                           usage_day_4=usage_day_4,
                           usage_week=usage_week_1,
                           usage_week_2=usage_week_2,
                           usage_week_3=usage_week_3,
                           usage_week_4=usage_week_4,
                           usage_month=usage_month_1,
                           usage_month_2=usage_month_2,
                           usage_month_3=usage_month_3,
                           usage_month_4=usage_month_4,
                           timestamp=current_timestamp_1,
                           timestamp_2=current_timestamp_2,
                           timestamp_3=current_timestamp_3,
                           timestamp_4=current_timestamp_4,
                           labels_hour_1=labels_hour_1,
                           values_hour_1=values_hour_1,
                           labels_week_1=labels_week_1,
                           values_week_1=values_week_1,
                           labels_month_1=labels_month_1,
                           values_month_1=values_month_1,
                           labels_hour_2=labels_hour_2,
                           values_hour_2=values_hour_2,
                           labels_week_2=labels_week_2,
                           values_week_2=values_week_2,
                           labels_month_2=labels_month_2,
                           values_month_2=values_month_2,
                           labels_hour_3=labels_hour_3,
                           values_hour_3=values_hour_3,
                           labels_week_3=labels_week_3,
                           values_week_3=values_week_3,
                           labels_month_3=labels_month_3,
                           values_month_3=values_month_3,
                           labels_hour_4=labels_hour_4,
                           values_hour_4=values_hour_4,
                           labels_week_4=labels_week_4,
                           values_week_4=values_week_4,
                           labels_month_4=labels_month_4,
                           values_month_4=values_month_4,
                           status_1=status_1,
                           status_2=status_2,
                           status_3=status_3,
                           status_4=status_4,
                           meter_type_1=meter_type_1,
                           meter_type_2=meter_type_2,
                           meter_type_3=meter_type_3,
                           meter_type_4=meter_type_4)

@views.route('/raw-data')
@login_required
def raw():
    return render_template("raw_data.html",
                           user=current_user,
                           first_name=current_user.first_name,
                           last_name=current_user.last_name,
                           meterId_1=current_user.meterID_1,
                           meterId_2=current_user.meterID_2,
                           meterId_3=current_user.meterID_3,
                           meterId_4=current_user.meterID_4)

@views.route('/manage-meters')
@login_required
def meter_manage():
    return render_template("manage_meter.html",
                           user=current_user,
                           first_name=current_user.first_name,
                           last_name=current_user.last_name)
