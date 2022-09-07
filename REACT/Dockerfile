FROM debian:latest

SHELL ["/bin/bash", "--login", "-c"]

LABEL Meriem Boughezzi <mariem.bouguezzi@gmail.com>

RUN apt update && \
    apt install curl vim wget -y && \
    cp -R /etc/vim/vimrc ~/.vimrc && \
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash && \
    echo 'NVM_DIR="$HOME/.nvm"' >> ~/.bashrc && \
    echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm' >> ~/.bashrc && \
    echo '[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion' >> ~/.bashrc

RUN nvm install node && \
    nvm install 16.17.0 && \
    nvm use 16.17.0 && \
    nvm alias default 16.17.0
    
ADD . /opt/

RUN ls /opt && \
    chmod +x /opt/start.sh

ENTRYPOINT ["/opt/start.sh"]
CMD ["0.0.0.0"]

