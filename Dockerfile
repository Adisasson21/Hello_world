FROM ubuntu
RUN apt-get update
RUN apt-get install -y python python-pip
RUN pip install flask
COPY flask_func.py /opt/flask_func.py
ENTRYPOINT Flask_APP= /opt/flask_func.py flask run --host=0.0.0.0
