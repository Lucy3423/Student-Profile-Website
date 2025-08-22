from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


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


new_bulletin_notice = Bulletin_notice("11/08/2025", "School Uniform Update", "upper 4", "We have recently changed the school uniform to allow girls in all year groups to wear trousers instead of the skirt if they wish to.")
system.bulletin_notices.append(new_bulletin_notice)
new_bulletin_notice = Bulletin_notice("09/08/2025", "Pack Lunches", "all", "This is a reminder that if your child wishes to have pack lunches next term, you must opt out of school lunches by 20/08/2025. Failing to do so will lead to automatique payment for the next term's lunches at school.")
system.bulletin_notices.append(new_bulletin_notice)
new_bulletin_notice = Bulletin_notice("20/08/2025", "Halloween Disco", "upper 6", "There will be a Halloween disco next Friday (29/08/25) starting at 6:30pm until 8pm. Students are encouraged to dress up in fun costumes for the event.")
system.bulletin_notices.append(new_bulletin_notice)


@app.route("/dashboard/<int:student_id>")
def dashboard(student_id):
    student = system.find_student(student_id)
    print(student.student_id)
    return render_template("dashboard.html", student=student, student_id=student_id)



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
    print(sort_type)
    return render_template("bulletin.html", bulletin_notices=system.bulletin_notices, student_id=student_id, sort_form=sort_form, sort_type=sort_type)


@app.route('/clubs/<int:student_id>')
def clubs(student_id):
    return render_template("clubs.html", student_id=student_id, system=system)


if __name__ == "__main__":
    app.run(debug=True)  
