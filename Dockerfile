FROM python:3.8-alpine
ENV PATH = "/scripts:${PATH}"
#Copy requirements.txt to the image
COPY ./requirements.txt /requirements/txt

#install dependencies to install requirements
#.tmp is used to install these dependencies and deleted later
RUN apt add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

RUN pip install -r /requirement.txt

#delete requirements.txt
RUN apk del .tmp

#create app folder
RUN mkdir /app

#copy project to the app folder
COPY ./employeeSystem /app

#specify working directory
WORKDIR /app

COPY ./scripts /scripts

#give permission to run scripts
RUN chmod +x /scripts/*

#create media and static directories
RUN mkdir -p /vol/web/media

RUN mkdir -p /vol/web/static

#create user

RUN adduser -D user

RUN chown -R user:user /vol

RUN chmod -R 755 /vol/web

USER user

CMD ["entrypoint.sh"]


