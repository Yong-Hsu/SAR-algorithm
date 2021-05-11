FROM python:3.7.3

COPY requirements.txt /
#RUN apt-get update -y
#RUN apt-get -y install libglib2.0-0 libsm6 libxrender1 libfontconfig1
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["./gunicorn.sh"]
