FROM python:3.7.3-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt
RUN sudo apt-get install libglib2.0-0

COPY . /app
WORKDIR /app

ENTRYPOINT ["./gunicorn.sh"]
