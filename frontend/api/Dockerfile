FROM python:3.6.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN rm -f db.sqlite3
RUN python3 manage.py migrate
RUN python3 manage.py generate
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 80