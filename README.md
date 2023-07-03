# WebDeveloperTestWork
WebDeveloperTestWork

# Проект Foodgram

### Описание
Проект "Foodgram" – это "продуктовый помощник". На этом сервисе авторизированные пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное». Для неавторизированных пользователей доступны просмотр рецептов и страниц авторов.

Проект запущен по адресу: http://158.160.107.15/

Админка
Login: admin
Password: admin
mail: admin@admin.ru

### Как запустить проект на боевом сервере:

Установить на сервере docker и docker-compose. Скопировать на сервер файлы docker-compose.yaml и default.conf:

```
scp docker-compose.yml <логин_на_сервере>@<IP_сервера>:/home/sarymov/docker-compose.yml
scp nginx.conf <логин_на_сервере>@<IP_сервера>:/home/sarymov/nginx/nginx.conf

```

Добавить в Secrets на Github следующие данные:

```
