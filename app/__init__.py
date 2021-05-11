from flask import Flask
from sar.main import matrix_prob_608
import logging
import sys

app = Flask(__name__)

from app import views


@app.route('/servCheck', methods=['GET', 'POST'])
def service_status():
    return {'status': '1'}


@app.route('/608test', methods=['GET', 'POST'])
def matrix608_send():
    return {'matrix_prob': matrix_prob_608()}


@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)
