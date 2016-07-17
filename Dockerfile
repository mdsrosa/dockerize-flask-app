FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD ./app/ /app
RUN pip install -r requirements.txt
