from flask import render_template
from app import app
from sar import main


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/servCheck', methods=['GET', 'POST'])
def service_status():
    return {'status': '1'}


@app.route('/608test', methods=['GET', 'POST'])
def matrix608_send():
    return {'matrix_prob': main.matrix_prob_608()}
