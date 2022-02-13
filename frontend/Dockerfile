FROM node:lts-buster-slim
ENV APP_ROOT /code
WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
RUN npm ci
ENV HOST 0.0.0.0