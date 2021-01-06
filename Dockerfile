FROM python:3-alpine as builder

COPY requirements.txt ./

RUN apk update && \
    apk upgrade && \
    apk --update add --virtual build-dependencies gcc musl-dev libffi-dev openssl-dev libxml2 libxml2-dev libxslt-dev && \
    pip install --no-cache-dir --root=/app -r requirements.txt

from python:3-alpine as latest

COPY --from=builder /app /

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./main.py" ]