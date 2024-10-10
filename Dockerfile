FROM alpine:latest

WORKDIR /app

COPY . /app

RUN echo "http://mirrors.aliyun.com/alpine/v3.16/main/" > /etc/apk/repositories && \
    echo "http://mirrors.aliyun.com/alpine/v3.16/community/" >> /etc/apk/repositories

RUN apk add --no-cache python3 py3-pip npm 

RUN pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple/ 

RUN chmod +x start.sh

EXPOSE 5173
EXPOSE 8080

CMD ["./start.sh"]
