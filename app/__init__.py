from flask import Flask
from sar import main
import numpy as np

app = Flask(__name__)

from app import views


@app.route('/servCheck', methods=['GET', 'POST'])
def service_status():
    return {'status': '1'}


@app.route('/608test', methods=['GET', 'POST'])
def matrix608_send():
    return {'matrix_prob': main.matrix_prob_608()}
