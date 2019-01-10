FROM  python:2-slim-stretch
MAINTAINER  sinan <zhihao.fang@yitu-inc.com>

RUN apt update && apt install -y curl  gnupg && \
    echo "deb http://hwraid.le-vert.net/debian stretch main" >> /etc/apt/sources.list && \
    curl  http://hwraid.le-vert.net/debian/hwraid.le-vert.net.gpg.key | apt-key add - && \
    apt update && apt install -y megacli -y && \
    apt purge gnupg curl -y && apt autoremove -y && apt autoclean -y && \
    pip install flask

COPY app /app/
EXPOSE 80
ENTRYPOINT ["python", "/app/app.py"]
