from flask import Flask
from flask import render_template

from flask import json, request

app = Flask(__name__)


@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/fill_in')
def fill_in_page():
	return render_template('fill_in.html')

@app.route('/display')
def display_page():
	return render_template('display_mad_lib.html')


if __name__ == '__main__':
    app.run()