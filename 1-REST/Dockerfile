FROM ubuntu:latest
MAINTAINER Hossameldin Ali "hossameldin_ali@outlook.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y libmysqlclient-dev
COPY . /main
WORKDIR /main
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
