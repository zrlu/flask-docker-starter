FROM python:3.9
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY src/ /app
WORKDIR /app
ENV FLASK_APP app
ENV FLASK_ENV debug
ENV FLASK_DEBUG 1
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000
CMD ["flask", "run"]