FROM python:3.10.9

# Declared Environment Variables
ENV PMS=/var/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory, where the commands will be ran:
RUN mkdir -p $PMS
WORKDIR $PMS

# Adding Packages
RUN pip install django
RUN pip install pillow
RUN pip install psycopg
RUN pip install gunicorn
ADD ./static /static
ADD . .

ADD docker/app/entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "proactive.wsgi"]