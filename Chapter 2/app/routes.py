from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm
@app.route('/')
@app.route('/index')



def index():
    user = {'username': 'Chrys'}
    posts = [
        {
            'author': {'username': 'dmitry'},
            'body' : 'Drink vodka for babushka'
        },
        {
            'author': {'username': 'gluvnoski'},
            'body' : 'Brrrrrr gun shot in babushka frontyard'
        }

    ]
    return render_template('index.html' , title='Home', user=user , posts=posts)

@app.route('/page2')
def page2():
    info = {'info':'this is page 2 route'}
    return render_template('page2.html' , info = info)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect((url_for('index')))
    return render_template('login.html', title='Sign In', form=form)

