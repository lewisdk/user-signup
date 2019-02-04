from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

signup_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Signup</h1>
    <form action="/add" method = "post">
  
        <label for="username">Username:</label>
        <input id="username" type="text" name="username"/>
        <p class="error">{username_error}</p>
        </br>
        <label for="password" >Password:</label>
        <input id="password" type="password" name="password"/>
        <p class="error">{password_error}</p>
        </br>
        <label for="verify">Verify password:</label>
        <input id="verify" type="password" name="verfiy"/>
        <p class="error">{verify_error}</p>
        </br>
        <label for="email">Email (optional):</label>
        <input id="email" type="text" name="email"/>
        <p class="error">{email_error}</p>
        </br>
        <button type="submit">Submit</button>
    </form>
    </body>
    </html>
</html>
"""            
@app.route("/", methods =['POST'])
def index():
    return form  

def username():
    if not len(username)>3 and len(username)<20:
        return error


app.run()