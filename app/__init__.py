from flask import Flask
from main import matrix_prob_608, fast_matrix
import logging
# from flask.ext.cors import CORS

app = Flask(__name__)
# CORS(app)

from app import views


@app.route('/servCheck', methods=['GET', 'POST'])
def service_status():
    return {'status': '1'}


@app.route('/608test', methods=['GET', 'POST'])
def matrix608_send():
    return {'matrix_prob': matrix_prob_608().tolist()}


@app.route('/608fast', methods=['GET', 'POST'])
def fast608():
    return {fast_matrix().tolist()}


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response
