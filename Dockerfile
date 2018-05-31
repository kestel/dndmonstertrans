FROM python:3.6-alpine

ADD requirements.txt /tmp/

RUN apk update && apk add build-base && \
    pip3 install -r /tmp/requirements.txt
    COPY . .

ENTRYPOINT ["python3", "translate_web.py", "8080"]
CMD ['']
