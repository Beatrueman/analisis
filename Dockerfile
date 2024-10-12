FROM alpine:latest

WORKDIR /app

COPY . /app

RUN echo "http://mirrors.aliyun.com/alpine/v3.16/main/" > /etc/apk/repositories && \
    echo "http://mirrors.aliyun.com/alpine/v3.16/community/" >> /etc/apk/repositories && \
    apk add --no-cache python3 py3-pip npm && \
    pip3 install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple/ && \
    chmod +x start.sh

EXPOSE 5173
EXPOSE 8080

CMD ["./start.sh"]
