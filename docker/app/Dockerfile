FROM python:3.7

# Declared Environment Variables
ENV PROACTIVE=/var/app
ENV SECRET_KEY='django-insecure-kcj#v#0s^l@s^=&lztvigrso4rv%u^*3zj+@%@kxu8!t8qy(o5'
ENV DEBUG=false
ENV DATABASE_NAME=proactive
ENV DATABASE_USER=postgres
ENV DATABASE_PASSWORD=
ENV DATABASE_HOST=postgres
ENV DATABASE_PORT=5432
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory, where the commands will be ran:
RUN mkdir -p $PROACTIVE
WORKDIR $PROACTIVE

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