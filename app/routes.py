from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm

@app.route("/")
def index():
    
    
@app.route('/register')
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        name = form.name.data
        phone_number = form.phone.data
        address = form.address.data
        print(name, phone_number, address)
        flash('You have successfully signed up!', 'success')
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)