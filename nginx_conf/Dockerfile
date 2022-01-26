FROM nginx:alpine

ARG UID
ARG GID

COPY nginx.conf /etc/nginx/nginx.conf
COPY default/default.conf /etc/nginx/conf.d/default.conf

RUN apk add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    echo "Asia/Tokyo" > /etc/timezone && \
    apk del tzdata

RUN touch /var/run/nginx.pid && \
  chown -R ${UID}:${GID} /var/run/nginx.pid && \
  chown -R ${UID}:${GID}  /var/cache/nginx