from flask import Flask, request, render_template, jsonify, redirect, session, send_from_directory
import requests
from datetime import datetime

app = Flask(__name__)




@app.route('/')
def map():
    return render_template('map.html')


@app.route('/beaches')
def beaches():
    return render_template('info.html')



@app.route('/data')
def data():
    return render_template('data.html')



@app.route('/resources')
def resources():
    return render_template('resources.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
