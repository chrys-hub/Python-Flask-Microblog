from app import app
from flask import render_template
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
