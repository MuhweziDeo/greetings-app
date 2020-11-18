FROM python:3.7


RUN mkdir app

COPY . /app/


WORKDIR /app


RUN pip install -r requirements.txt

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]
