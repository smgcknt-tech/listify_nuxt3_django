FROM python:3.8-slim
ARG UID
ARG GID
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /code
WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN python manage.py collectstatic --no-input


