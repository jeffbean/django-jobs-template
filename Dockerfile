FROM python:3.3
MAINTAINER jeffreyrobertbean@gmail.com

# create unprivileged user
RUN adduser --disabled-password --gecos '' djuser

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code


RUN pip install ipython
ADD test_requirements.txt /code/
RUN pip install -r test_requirements.txt

ADD requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
CMD ./run_web.sh