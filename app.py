from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'apples123'
app.debug = True
toolbar = DebugToolbarExtension(app)

@app.route('/')
def index():
    return 'Hello, world!'