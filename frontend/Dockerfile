FROM node:20-alpine AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install --no-audit --no-fund

COPY public ./public
COPY src ./src

ARG REACT_APP_GOOGLE_CLIENT_ID
ENV REACT_APP_GOOGLE_CLIENT_ID=${REACT_APP_GOOGLE_CLIENT_ID}
ENV REACT_APP_API_PROCESS_LOGIN=/api/login \
    REACT_APP_API_PROCESS_LOGIN_GG=/api/login-google \
    REACT_APP_API_NOTES=/api/get-notes \
    REACT_APP_API_ADD_NOTE=/api/create-note \
    REACT_APP_API_DELETE_NOTE=/api/delete-note \
    REACT_APP_API_UPDATE_NOTE=/api/notes/update \
    REACT_APP_API_IMAGE_UPLOAD=/api/upload-image

RUN npm run build

FROM nginx:alpine

COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80
