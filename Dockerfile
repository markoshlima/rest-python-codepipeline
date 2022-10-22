FROM python:3.7.10-alpine

RUN pip install pipenv

RUN pipenv --three

RUN pipenv install flask

RUN pipenv install marshmallow

COPY . .

RUN chmod +x ./bootstrap.sh

EXPOSE 8080

CMD ["./bootstrap.sh"]