FROM alpine:3.19
RUN apk add --no-cache busybox-extras
WORKDIR /var/www
COPY index.html .
EXPOSE 80
CMD ["httpd", "-f", "-p", "80", "-h", "/var/www"]
