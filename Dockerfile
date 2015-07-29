FROM ubuntu:latest
MAINTAINER V Lall "vishal.h.lall@gmail.com"

RUN apt-get clean && apt-get update && apt-get install -y \
	python-dev \
	python-pip 

RUN pip install \
	bokeh \
	numpy \
	pandas
