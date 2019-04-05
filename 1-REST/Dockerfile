FROM ubuntu:latest
MAINTAINER Hossameldin Ali "hossameldin_ali@outlook.com"
RUN apt-get update -y
#RUN apt-get install python3.6 -y
RUN apt-get install -y python-pip #python3-dev build-essential
RUN apt-get install -y libmysqlclient-dev
COPY . /usr/src/app
WORKDIR /usr/src/app
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
