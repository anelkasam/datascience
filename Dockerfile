FROM jupyter/all-spark-notebook

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
#RUN apt-get install openjdk-8-jdk-headless -qq

VOLUME /notebooks
WORKDIR /notebooks

