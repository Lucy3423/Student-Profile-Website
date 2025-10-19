from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from datetime import *


from student import Student 
from system import System
from bulletin_notice import Bulletin_notice
from forms.login_form import Login_form 
from forms.bulletin_sort_form import Bulletin_sort_form



app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

system = System()
system.set_up_students()
system.set_up_clubs()
system.set_up_bulletin_entries()


@app.route("/dashboard/<int:student_id>")
def dashboard(student_id):
    student = system.find_student(student_id)
    # find the current day and time
    day = datetime.today()
    # refine to only store the date rather than the time as well
    date = day.date() 
    date = date.strftime("%d/%m/%Y") # reorganise the date format 
    # find the current day of the week by its name
    current_day = day.strftime("%A") #A = full day (Monday), a = abbreviation (Mon)  
    # find the index of the day e.g. Mon = 0
    day_index = day.weekday()
    # get the current time and reformat it
    time = day.strftime("%H:%M:%S")
    # identify the correct time greeting
    greeting = system.identify_time_greeting(time)
    return render_template("dashboard.html", student=student, student_id=student_id, current_day=current_day, date=date, system=system, day_index=day_index, greeting=greeting)



@app.route('/student_profile/<int:student_id>')
def student_profile(student_id):
    student = system.find_student(student_id)
    return render_template('student_profile.html', student=student, subjects = student.subjects, student_id=student_id)


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = Login_form()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        found, student_id = system.login(username, password)
        if found == True:
            return redirect(url_for("dashboard", student_id=student_id))
        else:
            flash("""Incorrect username or password. Please re-enter""")
    
    return render_template("login_page.html", login_form=login_form)



@app.route('/bulletin/<int:student_id>', methods=["GET", "POST"])
def bulletin(student_id):
    sort_form = Bulletin_sort_form()
    sort_type = sort_form.sort_type.data
    # date = date.today()
    # print(date)
    return render_template("bulletin.html", bulletin_notices=system.bulletin_notices, student_id=student_id, sort_form=sort_form, sort_type=sort_type)


@app.route('/clubs/<int:student_id>', methods=["GET", "POST"])
def clubs(student_id):
    club_id = 100
    if request.method == "POST":
        club_id = int(request.form.get("club_id"))
        system.find_chosen_club(club_id, system.students[student_id])
    club_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return render_template("clubs.html", student_id=student_id, system=system, club_id=club_id, club_days = club_days)

@app.route('/flexbox')
def flexbox():
    return render_template("flexbox.html")



if __name__ == "__main__":
    app.run(debug=True)  
