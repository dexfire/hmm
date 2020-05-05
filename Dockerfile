FROM node:12.16.3

MAINTAINER dexfire29@foxmail.com
COPY . /app/
WORKDIR /app
RUN npm i
EXPOSE 80
CMD ["hexo", "server", "-p", "80"]