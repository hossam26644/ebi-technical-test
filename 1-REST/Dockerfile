FROM ubuntu:latest
MAINTAINER Hossameldin Ali "hossameldin_ali@outlook.com"
RUN apt-get update -y
RUN apt-get install python3.6 -y
RUN apt-get install -y python3-pip #python3-dev build-essential
RUN apt-get install -y libmysqlclient-dev
COPY . /usr/src/app
WORKDIR /usr/src/app
EXPOSE 5000
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
