FROM postgres:12

COPY init.sql /docker-entrypoint-initdb.d

#RUN pg_createcluster 12 main && service postgresql start
#RUN service postgresql start