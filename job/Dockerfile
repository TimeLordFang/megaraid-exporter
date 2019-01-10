FROM  debian:9-slim
MAINTAINER  TimeLordFang

RUN apt update && apt install -y curl  gnupg && \
    echo "deb http://hwraid.le-vert.net/debian stretch main" >> /etc/apt/sources.list && \
    curl  http://hwraid.le-vert.net/debian/hwraid.le-vert.net.gpg.key | apt-key add - && \
    apt update && apt install -y megacli megaclisas-status -y && \
    apt purge gnupg curl -y && apt autoremove -y && apt autoclean -y && \
    mkdir -p /data/promethues_text_collector/

COPY megacli.py /
ENTRYPOINT [ "/usr/bin/python" ]
CMD [ "/megacli.py" ]
