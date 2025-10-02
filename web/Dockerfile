FROM node:18-alpine
WORKDIR /usr/src/app
COPY ./nextjs-app/package.json ./
RUN npm install
COPY ./nextjs-app ./
CMD ["npm", "run", "dev"]
