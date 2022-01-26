FROM node:lts-alpine
RUN apk update \
    && apk --no-cache add curl
ENV APP_ROOT /code
WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
ENV HOST 0.0.0.0