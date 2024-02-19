FROM python:3.7

# Declared Environment Variables
ENV PMS=/var/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory, where the commands will be ran:
RUN mkdir -p $PMS
WORKDIR $PMS

ADD requirements.txt requirements.txt

# Adding Packages
RUN pip install -r requirements.txt
ADD . .
RUN python manage.py collectstatic --noinput
ADD docker/app/entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "proactive.wsgi"]