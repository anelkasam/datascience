FROM jupyter/datascience-notebook

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

VOLUME /notebooks
WORKDIR /notebooks
