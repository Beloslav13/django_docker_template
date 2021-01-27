FROM redis:3.2.11

EXPOSE 6379

RUN mkdir /etc/redis
RUN mkdir /var/redis
RUN mkdir /var/run/redis
RUN mkdir /var/log/redis

COPY ./conf/redis.conf /etc/redis/redis.conf