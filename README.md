# How to start

## 1. Build, run and test using Docker

If you have docker, you can run the following in your host machine:

```bash
docker build . -t flask
docker run -d -p 80:5000 --name my_container flask:latest
```

In your the machine:

```bash
curl http://localhost/api/ping
```

To run tests:

```bash
docker exec my_container pytest -v
```

## 2. Build, run and test without Docker

```bash
pip install -r /requirements.txt
cd app
export FLASK_APP=app
flask run
```

In another terminal:

```bash
curl http://localhost/api/ping
```

To run tests:

```bash
# under app/
pytest -v
```
