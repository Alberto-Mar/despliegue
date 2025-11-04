# Dockerfile
FROM httpd:2.4
RUN a2enmod ssl
# Copiar certificado y clave
COPY certs/server.crt /usr/local/apache2/conf/server.crt
COPY certs/server.key /usr/local/apache2/conf/server.key
# Copiar configuración personalizada
COPY ssl.conf /usr/local/apache2/conf/extra/ssl.conf
# Habilitar el sitio SSL
RUN echo "Include conf/extra/ssl.conf" >> /usr/local/apache2/conf/httpd.conf
