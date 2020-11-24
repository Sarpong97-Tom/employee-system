# FROM python:3.8-alpine
# ENV PATH = "/scripts:${PATH}"
# #Copy requirements.txt to the image
# COPY ./requirements.txt /requirements.txt

# #install dependencies to install requirements
# #.tmp is used to install these dependencies and deleted later
# # RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers


# RUN pip install -r /requirements.txt

# #delete requirements.txt
# RUN apk del .tmp

# #create app folder
# RUN mkdir /app

# #copy project to the app folder
# COPY ./employeeSystem /app

# #specify working directory
# WORKDIR /app

# COPY ./scripts /scripts

# #give permission to run scripts
# RUN chmod +x /scripts/*

# #create media and static directories
# RUN mkdir -p /vol/web/media

# RUN mkdir -p /vol/web/static

# #create user

# RUN adduser -D user

# RUN chown -R user:user /vol

# RUN chmod -R 755 /vol/web

# USER user

# CMD ["entrypoint.sh"]


# Base Image
FROM python:3.8

ENV PATH = "/scripts:${PATH}"
#Copy requirements.txt to the image
COPY ./requirements.txt /requirements.txt


# create and set working directory
RUN mkdir /app
WORKDIR /app

COPY ./scripts /scripts

#give permission to run scripts
RUN chmod +x /scripts/*

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000

# Install system dependencies
RUN apt-get upgrade && apt-get install -y --no-install-recommends \
        tzdata \
        # python3-setuptools \
        # python3-pip \
        # python3-dev \
        # python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip 

# Install project dependencies
RUN pip3 install -r requirements.txt


#create media and static directories
RUN mkdir -p /vol/web/media

RUN mkdir -p /vol/web/static

#create user

RUN adduser user

RUN chown -R user:user /vol

RUN chmod -R 755 /vol/web

USER user

EXPOSE 8888
CMD gunicorn employeeSystem.wsgi:application --bind 0.0.0.0:$PORT
CMD ["python manage.py runserver"]