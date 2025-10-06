FROM ubuntu:24.04

RUN apt update \
&& apt install -y apache2 \
&& rm -rf /var/lib/apt/lists/*

# COPY index.html /var/www/html/index.html
# COPY portfolioapp

EXPOSE 80

CMD  ["apache2ctl", "-D", "FOREGROUND"]