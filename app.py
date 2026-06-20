# Flask App
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
#error for checking
if or else run

@app.route('/health')
def health():
    return 'Server is up and running'
