# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index (1).html')