import email
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Status: Logged in Successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Error: Password is incorrect, try again', category='error')
        else:
            flash('Error: Email not associated with an account', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email= request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        meterID_1 = 00000000
        meterID_2 = 00000000
        meterID_3 = 00000000
        meterID_4 = 00000000


        user = User.query.filter_by(email=email).first()
        if user:
            flash('Error: Email is already associated with an account', category='error')
        elif len(email) < 4:
            flash('Error: Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('Error: First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Error: Passwords do not match', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(
                password1, method='sha256'), meterID_1=meterID_1, meterID_2=meterID_2, meterID_3=meterID_3, meterID_4=meterID_4)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))


    return render_template("sign_up.html", user=current_user)

@auth.route('/manage-meters', methods=['GET', 'POST'])
@login_required
def manage_meters():
    if request.method == 'POST' and "add_meterId" in request.form:
        meterID = request.form.get('add_meterId')

        if len(meterID) != 8:
            flash('Error: Meter ID Must Be 8 Digits Long', category='error')
        elif current_user.meterID_1 == 00000000:
            current_user.meterID_1 = meterID
            db.session.commit()
            flash('Meter ID Added Successfully!', category='success')
        elif current_user.meterID_2 == 00000000:
            current_user.meterID_2 = meterID
            db.session.commit()
            flash('Meter ID Added Successfully!', category='success')
        elif current_user.meterID_3 == 00000000:
            current_user.meterID_3 = meterID
            db.session.commit()
            flash('Meter ID Added Successfully!', category='success')
        elif current_user.meterID_4 == 00000000:
            current_user.meterID_4 = meterID
            db.session.commit()
            flash('Meter ID Added Successfully!', category='success')
        else:
            flash('Error: Account cannot exceed 4 meter ID\'s', category='error')
        return redirect(url_for('auth.manage_meters'))
    else:
        meterID = request.form.get('del_meterId')
        if len(meterID) != 8:
            flash('Error: Meter ID Must Be 8 Digits Long', category='error')
        elif str(current_user.meterID_1) == meterID:
            current_user.meterID_1 = 00000000
            db.session.commit()
            flash('Meter ID Removed From Account!', category='warning')
        elif str(current_user.meterID_2) == meterID:
            current_user.meterID_2 = 00000000
            db.session.commit()
            flash('Meter ID Removed From Account!', category='warning')
        elif str(current_user.meterID_3) == meterID:
            current_user.meterID_3 = 00000000
            db.session.commit()
            flash('Meter ID Removed From Account!', category='warning')
        elif str(current_user.meterID_4) == meterID:
            current_user.meterID_4 = 00000000
            db.session.commit()
            flash('Meter ID Removed From Account!', category='warning')
        else:
            flash('Error: Meter ID Entered Is Not Associated With Account', category='error')
        return redirect(url_for('auth.manage_meters'))
