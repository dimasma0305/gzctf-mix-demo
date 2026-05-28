FROM alpine:3.19
RUN apk add --no-cache socat
COPY serve.sh /serve.sh
RUN chmod +x /serve.sh
EXPOSE 80
CMD ["socat", "-T", "5", "TCP-LISTEN:80,reuseaddr,fork", "EXEC:/serve.sh"]
