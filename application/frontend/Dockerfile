FROM node:16

ENV NODE_ENV=development
ENV PATH=/root/.yarn/bin:$PATH

WORKDIR /app

COPY ["package.json", "./"]

RUN yarn install
RUN yarn global add vite

COPY . .

EXPOSE 5000
EXPOSE 24678

CMD ["vite", "--host", "0.0.0.0"]
#CMD ["yarn", "global", "list"]
