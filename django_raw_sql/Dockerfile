FROM python:3.9

WORKDIR /var/www/project

ENV PGCONNECT_TIMEOUT 10

# Install requirements
COPY ./requirements.txt ./
RUN pip3 install -r ./requirements.txt

# Bundle app source
COPY . .

CMD python manage.py runserver
