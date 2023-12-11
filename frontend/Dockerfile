# build env
#FROM node:18-alpine
#WORKDIR /app
#COPY package*.json ./
#RUN npm install
#COPY . ./
#RUN npm run build
#CMD ["npm", "start"] #cp -r build result_build

FROM node:18-alpine

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем package.json и package-lock.json в контейнер
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

RUN npm install --save-dev typescript
# Копируем все файлы из текущей директории в контейнер
COPY . .

# Собираем React приложение
RUN npm run build

# Команда, которая будет запускаться при запуске контейнера на основе этого образа
CMD ["npm", "start"]