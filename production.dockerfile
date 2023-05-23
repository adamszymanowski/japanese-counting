# Stage 1: Build the Svelte app
FROM node:16 as build
WORKDIR /app
COPY ./frontend/package*.json ./
RUN npm install
COPY ./frontend ./
RUN npm run build --loglevel verbose


# Stage 2: Set up the web server
FROM nginx:1.24
COPY --from=build /app/dist /usr/share/nginx/html
COPY ./webserver/nginx.conf /etc/nginx/nginx.conf