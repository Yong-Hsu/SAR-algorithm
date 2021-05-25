# sar-web

https://itnext.io/setup-flask-project-using-docker-and-gunicorn-4dcaaa829620


chmod +x gunicorn.sh

docker build -t flask/flask_docker .
docker run -d -p 80:80 flask/flask_docker .

