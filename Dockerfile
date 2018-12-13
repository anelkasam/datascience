FROM jupyter/datascience-notebook

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt

VOLUME /notebooks
WORKDIR /notebooks

#FROM jupyter/all-spark-notebook
#ADD . /code
#WORKDIR /code
#RUN pip install -r requirements.txt
#CMD ["jupyter notebook"]
