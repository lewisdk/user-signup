from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Signup</title>
    </head>
    <body>    
        <h1>Signup</h1>

"""
page_footer = """
    </body>
</html>
"""

add_form = """
    <form action="/add" method = "post">
  
        <label for="username">Username:</label>
        <input id="username" type="text" name="username"/>
        </br>
        <label for="password" >Password:</label>
        <input id="password" type="password" name="password"/>
        </br>
        <label for="verify">Verify password:</label>
        <input id="verify" type="password" name="verfiy"/>
        </br>
        <label for="email">Email (optional):</label>
        <input id="email" type="text" name="email"/>
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