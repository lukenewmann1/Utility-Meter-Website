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
        if not os.path.isfile("C:\\meter_tmp\\"+(str(current_user.meterID_1)+".csv")):
            status_1 = 0
        else:
            meterID_1_hour = hour(current_user.meterID_1)
            meterID_1_day = day(current_user.meterID_1)
            meterID_1_month = month(current_user.meterID_1)
            current_timestamp_1 = timestamp(current_user.meterID_1)
            meter_type_1 = int(meterType(current_user.meterID_1))
            axis_hour_1 = axisHour(current_user.meterID_1)
            axis_week_1 = axisWeek(current_user.meterID_1)
            axis_month_1 = axisMonth(current_user.meterID_1)

            if meter_type_1 == 12 or meter_type_1 == 156 or meter_type_1 == 11:
                meter_type_1 = "Gas"
            elif meter_type_1 == 13 or meter_type_1 == 203:
                meter_type_1 = "Water"
            elif meter_type_1 == 5:
                meter_type_1 = "Electricity"
            elif meter_type_1 == 0:
                meter_type_1 = "{Error: Null Value}"
            else:
                meter_type_1 = "{Error: Undefined Value}"

            if meterID_1_hour != 3:
                usage_hour_1 = meterID_1_hour[0]
                data_hour = [(axis_hour_1[23],meterID_1_hour[23]),(axis_hour_1[22],meterID_1_hour[22]),(axis_hour_1[21],meterID_1_hour[21]),(axis_hour_1[20],meterID_1_hour[20]),
                             (axis_hour_1[19],meterID_1_hour[19]),(axis_hour_1[18],meterID_1_hour[18]),(axis_hour_1[17],meterID_1_hour[17]),(axis_hour_1[16],meterID_1_hour[16]),
                             (axis_hour_1[15],meterID_1_hour[15]),(axis_hour_1[14],meterID_1_hour[14]),(axis_hour_1[13],meterID_1_hour[13]),(axis_hour_1[12],meterID_1_hour[12]),
                             (axis_hour_1[11],meterID_1_hour[11]),(axis_hour_1[10],meterID_1_hour[10]),(axis_hour_1[9],meterID_1_hour[9]),(axis_hour_1[8],meterID_1_hour[8]),
                             (axis_hour_1[7],meterID_1_hour[7]),(axis_hour_1[6],meterID_1_hour[6]),(axis_hour_1[5],meterID_1_hour[5]),(axis_hour_1[4],meterID_1_hour[4]),
                             (axis_hour_1[3],meterID_1_hour[3]),(axis_hour_1[2],meterID_1_hour[2]),(axis_hour_1[1],meterID_1_hour[1]),(axis_hour_1[0],meterID_1_hour[0])]
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
                data_week = [(axis_week_1[6],meterID_1_day[6]),(axis_week_1[5],meterID_1_day[5]),(axis_week_1[4],meterID_1_day[4]),
                             (axis_week_1[3],meterID_1_day[3]),(axis_week_1[2],meterID_1_day[2]),(axis_week_1[1],meterID_1_day[1]),
                             (axis_week_1[0],meterID_1_day[0])]
                labels_week_1 = [row[0] for row in data_week]
                values_week_1 = [row[1] for row in data_week]
            else:
                usage_week_1 = "{Insufficient Data}"
                null_data_week = [("Mon.",0),("Tue.",0),("Wed",0),("Thu.",0),("Fri.",0),("Sat.",0),("Sun.",0)]
                labels_week_1 = [row[0] for row in null_data_week]
                values_week_1 = [row[1] for row in null_data_week]

            if meterID_1_month != 3:
                usage_month_1 = meterID_1_month[0]
                data_month = [(axis_month_1[11],meterID_1_month[11]),(axis_month_1[10],meterID_1_month[10]),(axis_month_1[9],meterID_1_month[9]),
                              (axis_month_1[8],meterID_1_month[8]),(axis_month_1[7],meterID_1_month[7]),(axis_month_1[6],meterID_1_month[6]),
                              (axis_month_1[5],meterID_1_month[5]),(axis_month_1[4],meterID_1_month[4]),(axis_month_1[3],meterID_1_month[3]),
                              (axis_month_1[2],meterID_1_month[2]),(axis_month_1[1],meterID_1_month[1]),(axis_month_1[0],meterID_1_month[0])]
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
        if not os.path.isfile("C:\\meter_tmp\\"+(str(current_user.meterID_2)+".csv")):
            status_2 = 0
        else:
            meterID_2_hour = hour(current_user.meterID_2)
            meterID_2_day = day(current_user.meterID_2)
            meterID_2_month = month(current_user.meterID_2)
            current_timestamp_2 = timestamp(current_user.meterID_2)
            meter_type_2 = int(meterType(current_user.meterID_2))
            axis_hour_2 = axisHour(current_user.meterID_2)
            axis_week_2 = axisWeek(current_user.meterID_2)
            axis_month_2 = axisMonth(current_user.meterID_2)

            if meter_type_2 == 12 or meter_type_2 == 156 or meter_type_2 == 11:
                meter_type_2 = "Gas"
            elif meter_type_2 == 13 or meter_type_2 == 203:
                meter_type_2 = "Water"
            elif meter_type_2 == 5:
                meter_type_2 = "Electricity"
            elif meter_type_2 == 0:
                meter_type_2 = "{Error: Null Value}"
            else:
                meter_type_2 = "{Error: Undefined Value}"

            if meterID_2_hour != 3:
                usage_hour_2 = meterID_2_hour[0]
                data_hour = [(axis_hour_2[23],meterID_2_hour[23]),(axis_hour_2[22],meterID_2_hour[22]),(axis_hour_2[21],meterID_2_hour[21]),(axis_hour_2[20],meterID_2_hour[20]),
                             (axis_hour_2[19],meterID_2_hour[19]),(axis_hour_2[18],meterID_2_hour[18]),(axis_hour_2[17],meterID_2_hour[17]),(axis_hour_2[16],meterID_2_hour[16]),
                             (axis_hour_2[15],meterID_2_hour[15]),(axis_hour_2[14],meterID_2_hour[14]),(axis_hour_2[13],meterID_2_hour[13]),(axis_hour_2[12],meterID_2_hour[12]),
                             (axis_hour_2[11],meterID_2_hour[11]),(axis_hour_2[10],meterID_2_hour[10]),(axis_hour_2[9],meterID_2_hour[9]),(axis_hour_2[8],meterID_2_hour[8]),
                             (axis_hour_2[7],meterID_2_hour[7]),(axis_hour_2[6],meterID_2_hour[6]),(axis_hour_2[5],meterID_2_hour[5]),(axis_hour_2[4],meterID_2_hour[4]),
                             (axis_hour_2[3],meterID_2_hour[3]),(axis_hour_2[2],meterID_2_hour[2]),(axis_hour_2[1],meterID_2_hour[1]),(axis_hour_2[0],meterID_2_hour[0])]
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
                data_week = [(axis_week_2[6],meterID_2_day[6]),(axis_week_2[5],meterID_2_day[5]),(axis_week_2[4],meterID_2_day[4]),
                             (axis_week_2[3],meterID_2_day[3]),(axis_week_2[2],meterID_2_day[2]),(axis_week_2[1],meterID_2_day[1]),
                             (axis_week_2[0],meterID_2_day[0])]
                labels_week_2 = [row[0] for row in data_week]
                values_week_2 = [row[1] for row in data_week]
            else:
                usage_week_2 = "{Insufficient Data}"
                null_data_week = [("Mon.",0),("Tue.",0),("Wed",0),("Thu.",0),("Fri.",0),("Sat.",0),("Sun.",0)]
                labels_week_2 = [row[0] for row in null_data_week]
                values_week_2 = [row[1] for row in null_data_week]

            if meterID_2_month != 3:
                usage_month_2 = meterID_2_month[0]
                data_month = [(axis_month_2[11],meterID_2_month[11]),(axis_month_2[10],meterID_2_month[10]),(axis_month_2[9],meterID_2_month[9]),
                              (axis_month_2[8],meterID_2_month[8]),(axis_month_2[7],meterID_2_month[7]),(axis_month_2[6],meterID_2_month[6]),
                              (axis_month_2[5],meterID_2_month[5]),(axis_month_2[4],meterID_2_month[4]),(axis_month_2[3],meterID_2_month[3]),
                              (axis_month_2[2],meterID_2_month[2]),(axis_month_2[1],meterID_2_month[1]),(axis_month_2[0],meterID_2_month[0])]
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
        if not os.path.isfile("C:\\meter_tmp\\"+(str(current_user.meterID_3)+".csv")):
            status_3 = 0
        else:
            meterID_3_hour = hour(current_user.meterID_3)
            meterID_3_day = day(current_user.meterID_3)
            meterID_3_month = month(current_user.meterID_3)
            current_timestamp_3 = timestamp(current_user.meterID_3)
            meter_type_3 = int(meterType(current_user.meterID_3))
            axis_hour_3 = axisHour(current_user.meterID_3)
            axis_week_3 = axisWeek(current_user.meterID_3)
            axis_month_3 = axisMonth(current_user.meterID_3)

            if meter_type_3 == 12 or meter_type_3 == 156 or meter_type_3 == 11:
                meter_type_3 = "Gas"
            elif meter_type_3 == 13 or meter_type_3 == 203:
                meter_type_3 = "Water"
            elif meter_type_3 == 5:
                meter_type_3 = "Electricity"
            elif meter_type_3 == 0:
                meter_type_3 = "{Error: Null Value}"
            else:
                meter_type_3 = "{Error: Undefined Value}"

            if meterID_3_hour != 3:
                usage_hour_3 = meterID_3_hour[0]
                data_hour = [(axis_hour_3[23],meterID_3_hour[23]),(axis_hour_3[22],meterID_3_hour[22]),(axis_hour_3[21],meterID_3_hour[21]),(axis_hour_3[20],meterID_3_hour[20]),
                             (axis_hour_3[19],meterID_3_hour[19]),(axis_hour_3[18],meterID_3_hour[18]),(axis_hour_3[17],meterID_3_hour[17]),(axis_hour_3[16],meterID_3_hour[16]),
                             (axis_hour_3[15],meterID_3_hour[15]),(axis_hour_3[14],meterID_3_hour[14]),(axis_hour_3[13],meterID_3_hour[13]),(axis_hour_3[12],meterID_3_hour[12]),
                             (axis_hour_3[11],meterID_3_hour[11]),(axis_hour_3[10],meterID_3_hour[10]),(axis_hour_3[9],meterID_3_hour[9]),(axis_hour_3[8],meterID_3_hour[8]),
                             (axis_hour_3[7],meterID_3_hour[7]),(axis_hour_3[6],meterID_3_hour[6]),(axis_hour_3[5],meterID_3_hour[5]),(axis_hour_3[4],meterID_3_hour[4]),
                             (axis_hour_3[3],meterID_3_hour[3]),(axis_hour_3[2],meterID_3_hour[2]),(axis_hour_3[1],meterID_3_hour[1]),(axis_hour_3[0],meterID_3_hour[0])]
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
                data_week = [(axis_week_3[6],meterID_3_day[6]),(axis_week_3[5],meterID_3_day[5]),(axis_week_3[4],meterID_3_day[4]),
                             (axis_week_3[3],meterID_3_day[3]),(axis_week_3[2],meterID_3_day[2]),(axis_week_3[1],meterID_3_day[1]),
                             (axis_week_3[0],meterID_3_day[0])]
                labels_week_3 = [row[0] for row in data_week]
                values_week_3 = [row[1] for row in data_week]
            else:
                usage_week_3 = "{Insufficient Data}"
                null_data_week = [("Mon.",0),("Tue.",0),("Wed",0),("Thu.",0),("Fri.",0),("Sat.",0),("Sun.",0)]
                labels_week_3 = [row[0] for row in null_data_week]
                values_week_3 = [row[1] for row in null_data_week]

            if meterID_3_month != 3:
                usage_month_3 = meterID_3_month[0]
                data_month = [(axis_month_3[11],meterID_3_month[11]),(axis_month_3[10],meterID_3_month[10]),(axis_month_3[9],meterID_3_month[9]),
                              (axis_month_3[8],meterID_3_month[8]),(axis_month_3[7],meterID_3_month[7]),(axis_month_3[6],meterID_3_month[6]),
                              (axis_month_3[5],meterID_3_month[5]),(axis_month_3[4],meterID_3_month[4]),(axis_month_3[3],meterID_3_month[3]),
                              (axis_month_3[2],meterID_3_month[2]),(axis_month_3[1],meterID_3_month[1]),(axis_month_3[0],meterID_3_month[0])]
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
        if not os.path.isfile("C:\\meter_tmp\\"+(str(current_user.meterID_4)+".csv")):
            status_4 = 0
        else:
            meterID_4_hour = hour(current_user.meterID_4)
            meterID_4_day = day(current_user.meterID_4)
            meterID_4_month = month(current_user.meterID_4)
            current_timestamp_4 = timestamp(current_user.meterID_4)
            meter_type_4 = int(meterType(current_user.meterID_4))
            axis_hour_4 = axisHour(current_user.meterID_4)
            axis_week_4 = axisWeek(current_user.meterID_4)
            axis_month_4 = axisMonth(current_user.meterID_4)

            if meter_type_4 == 12 or meter_type_4 == 156 or meter_type_4 == 11:
                meter_type_4 = "Gas"
            elif meter_type_4 == 13 or meter_type_4 == 203:
                meter_type_4 = "Water"
            elif meter_type_4 == 5:
                meter_type_4 = "Electricity"
            elif meter_type_4 == 0:
                meter_type_4 = "{Error: Null}"
            else:
                meter_type_4 = "{Error: Undefined Value}"

            if meterID_4_hour != 3:
                usage_hour_4 = meterID_4_hour[0]
                data_hour = [(axis_hour_4[23],meterID_4_hour[23]),(axis_hour_4[22],meterID_4_hour[22]),(axis_hour_4[21],meterID_4_hour[21]),(axis_hour_4[20],meterID_4_hour[20]),
                             (axis_hour_4[19],meterID_4_hour[19]),(axis_hour_4[18],meterID_4_hour[18]),(axis_hour_4[17],meterID_4_hour[17]),(axis_hour_4[16],meterID_4_hour[16]),
                             (axis_hour_4[15],meterID_4_hour[15]),(axis_hour_4[14],meterID_4_hour[14]),(axis_hour_4[13],meterID_4_hour[13]),(axis_hour_4[12],meterID_4_hour[12]),
                             (axis_hour_4[11],meterID_4_hour[11]),(axis_hour_4[10],meterID_4_hour[10]),(axis_hour_4[9],meterID_4_hour[9]),(axis_hour_4[8],meterID_4_hour[8]),
                             (axis_hour_4[7],meterID_4_hour[7]),(axis_hour_4[6],meterID_4_hour[6]),(axis_hour_4[5],meterID_4_hour[5]),(axis_hour_4[4],meterID_4_hour[4]),
                             (axis_hour_4[3],meterID_4_hour[3]),(axis_hour_4[2],meterID_4_hour[2]),(axis_hour_4[1],meterID_4_hour[1]),(axis_hour_4[0],meterID_4_hour[0])]
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
                data_week = [(axis_week_4[6],meterID_4_day[6]),(axis_week_4[5],meterID_4_day[5]),(axis_week_4[4],meterID_4_day[4]),
                             (axis_week_4[3],meterID_4_day[3]),(axis_week_4[2],meterID_4_day[2]),(axis_week_4[1],meterID_4_day[1]),
                             (axis_week_4[0],meterID_4_day[0])]
                labels_week_4 = [row[0] for row in data_week]
                values_week_4 = [row[1] for row in data_week]
            else:
                usage_week_4 = "{Insufficient Data}"
                null_data_week = [("Mon.",0),("Tue.",0),("Wed",0),("Thu.",0),("Fri.",0),("Sat.",0),("Sun.",0)]
                labels_week_4 = [row[0] for row in null_data_week]
                values_week_4 = [row[1] for row in null_data_week]

            if meterID_4_month != 3:
                usage_month_4 = meterID_4_month[0]
                data_month = [(axis_month_4[11],meterID_4_month[11]),(axis_month_4[10],meterID_4_month[10]),(axis_month_4[9],meterID_4_month[9]),
                              (axis_month_4[8],meterID_4_month[8]),(axis_month_4[7],meterID_4_month[7]),(axis_month_4[6],meterID_4_month[6]),
                              (axis_month_4[5],meterID_4_month[5]),(axis_month_4[4],meterID_4_month[4]),(axis_month_4[3],meterID_4_month[3]),
                              (axis_month_4[2],meterID_4_month[2]),(axis_month_4[1],meterID_4_month[1]),(axis_month_4[0],meterID_4_month[0])]
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
