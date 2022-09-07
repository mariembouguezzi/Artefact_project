FROM python:3.7

SHELL ["/bin/bash", "--login", "-c"]

LABEL Meriem Boughezzi <mariem.bouguezzi@gmail.com>

RUN apt update && \
    apt install curl vim wget -y && \
    cp -R /etc/vim/vimrc ~/.vimrc

ADD . /opt/

RUN ls /opt && \
    chmod +x /opt/start.sh

ENTRYPOINT ["/opt/start.sh"]
CMD ["0.0.0.0"]