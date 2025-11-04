# Imagen base oficial con Apache y PHP preconfigurados
FROM php:8.2-apache
# Activar mod_rewrite
RUN a2enmod rewrite
# Copiar configuración personalizada del sitio
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
# Copiar archivo PHP de prueba
COPY . /var/www/html/
# Cambiar permisos si es necesario
RUN chown -R www-data:www-data /var/www/html
EXPOSE 80
# Comando por defecto
CMD ["apache2-foreground"]