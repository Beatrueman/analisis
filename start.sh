#!/bin/sh

# 启动Python
python3 app.py &

sleep 5

cd /app/fe/template 

npm install 

# 启动Node.js
npm run dev -- --host 
