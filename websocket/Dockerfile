FROM python:3.6.9-alpine
WORKDIR /code

RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime
ENV PORT 8000
EXPOSE 8000
COPY . .
CMD ["gunicorn", "--log-level=debug", "-k gevent", "-w 1", "app:app"]