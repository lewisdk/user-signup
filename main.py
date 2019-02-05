from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()         

@app.route("/good_username", methods=["POST"])
def good_username(username):
    username = request.form['username']

    if (len(username) > 3 and len(username) < 20):
        return True
    else:
        return False

@app.route("/good_password", methods=["POST"])
def good_password(password):
    password = request.form['password']

    if (len(password) > 3 and len(password) < 20):
        if not password.contains(" "):
            return True
    else:
        return False 

@app.route("/verify_password", methods=["POST"])
def password_match(verify):
    verify = request.form['verify']
    password = request.form['password']

    if [password] == [verify]:
        return True
    else:
        return False

@app.route("/good_email")
def good_email(email):

    email = request.form['email']
    if email != '':
        if email.match("[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False


@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error=''

    if good_username(username) != True:
        username_error = 'That is not a valid username.'
        username = ''

    if good_password(password) != True:
        password_error = 'That is not a valid password.'
        password = ''

    if password_match(verify) != True:
        verify_error = 'Passwords do not match.'
        verify = ''

    if good_email(email) != True:
        email_error = 'That is not a valid email address.'
        email = ''

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username'.format(username))
    else:
        template = jinja_env.get_template('index.html')
        return template.render(username_error = username_error, password_error = password_error, 
            verify_error = verify_error, email_error = email_error,
            username = username,
            password = '',
            verify = '',
            email = email)

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)

if __name__ == "__main__":
    app.run()