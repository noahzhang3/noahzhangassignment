
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Andrew from UNSW CODE!'