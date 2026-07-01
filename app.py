from flask import Flask, render_template, url_for, flash, redirect, request
import git
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'apples123'
app.debug = True
toolbar = DebugToolbarExtension(app)

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/flaskTestDeployed/flaskTest')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400