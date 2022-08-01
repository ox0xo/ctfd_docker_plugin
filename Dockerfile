FROM debian:stable-slim
COPY ./startup.sh /startup.sh
RUN apt-get update -y && apt-get install -y ssh bind9 vim
RUN mkdir /run/sshd
RUN chmod +x /startup.sh
RUN echo root:P@ssw0rd | chpasswd
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
EXPOSE 22 53
CMD ["/startup.sh"]
