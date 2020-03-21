# авторизация  
создание пользователей: http://127.0.0.1:8300/createUser  
Все пользователи могут просматривать товары  
Только авторизованные пользователи могут создовать товары  
Пользователи могут изменять только свои товары  
```
client_id = id  
client_secret = secret  
```
Пример получения токена:  
```
curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8300/oauth/token/
```
Пример обмена refresh token на новую пару access + refresh token:  
```
curl -X POST -d "grant_type=refresh_token&refresh_token=<your_refresh_token>&client_id=<client_id>&client_secret=<client_secret>" http://localhost:8300/oauth/token/
```
Также можно использовать Postman: ![a](https://i.ibb.co/3MXSN0y/10.png)

## REST API

Запускать командой `docker-compose up`  
Сайт поднимется на  http://127.0.0.1:8300/  

Есть пагинация (в данный момент 3 обекта на страницу)  
Все хранится в базе данных PostgreSQL  
При запуске docker-compose в консоль пишутся все логи обращений к api
