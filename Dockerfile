FROM ubuntu:latest
MAINTAINER Vlall

RUN apt-get clean && apt-get update && apt-get install -y \
	python-dev \
	python-pip 

RUN pip install \
	bokeh \
	numpy \
	pandas
