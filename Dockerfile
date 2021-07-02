FROM jupyter/all-spark-notebook

USER root

COPY requirements.txt /tmp
WORKDIR /tmp

RUN apt-get update

RUN pip install -r requirements.txt
#RUN apt-get apt-get install openjdk-8-jdk-headless -qq
RUN apt-get -y install graphviz

VOLUME /notebooks
WORKDIR /notebooks

