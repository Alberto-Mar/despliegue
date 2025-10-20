FROM ubuntu/apache2
RUN apt-get update && apt-get install -y apache2
# Activar mod_status
RUN a2enmod status
# Configurar el acceso al módulo
COPY ./config/apache2.conf /etc/apache2/apache2.conf
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
