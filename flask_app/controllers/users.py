from flask_app import app
from flask import render_template, redirect, flash, session, request
from .. models import user


@app.route('/')
def show_form():
    return render_template("form.html")


@app.route('/create', methods=['post'])
def add():
    if not user.User.validate_email(request.form):
        return redirect('/')

    user.User.add(request.form)
    return redirect("/success")


@app.route('/success')
def users():
    users = user.User.get_all()
    return render_template("show_emails.html", all_users=users)


@app.route('/destroy/<int:id>')
def delete_user(id):
    data = {
        "id": id
    }

    user.User.delete(data)
    return redirect('/success')
