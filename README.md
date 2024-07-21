Тестовое задание: Python Developer

## Пояснительная записка

<details>
  <summary>Пояснительная записка</summary>
  Так как до этого я не работал с S3, и в ТЗ это не обговаривается явно,
  то S3 я использовал только как хранилище изображений. Ссылки же на изображения
  храню в СУБД. В АПИ вместо самих изображений отдаю ссылки, по которым
  можно получить само изображение.
</details>

## Запуск проекта

Скачайте репозиторий:

~~~shell
git clone https://github.com/Masynchin/mad-soft-test-task.git
cd mad-soft-test-task
~~~

Запустите проект с помощью Docker Compose:

~~~shell
docker compose up --detach
~~~

После этого API станет доступным по адресу `http://localhost:8000`,
документация проекта по адресу `http://localhost:8000/docs`

Просмотр изображений по их `image_url` происходит по адресу
`http://localhost:8000/image/{image_url}`.

## ТЗ

Разработайте веб-приложение на Python, используя FastAPI, которое предоставляет
API для работы с коллекцией мемов. Приложение должно состоять из двух сервисов:
сервис с публичным API с бизнес-логикой и сервис для работы с медиа-файлами,
используя S3-совместимое хранилище (н-р, MinIO).
 
### Функциональность

- `GET /memes`: Получить список всех мемов (с пагинацией).
- `GET /memes/{id}`: Получить конкретный мем по его ID.
- `POST /memes`: Добавить новый мем (с картинкой и текстом).
- `PUT /memes/{id}`: Обновить существующий мем.
- `DELETE /memes/{id}`: Удалить мем. 

### Требования

- [x] Используйте реляционную СУБД для хранения данных.
- [x] Обеспечьте обработку ошибок и валидацию входных данных.
- [x] Используйте Swagger/OpenAPI для документирования API.
- [ ] Напишите хотя бы несколько unit-тестов для проверки основной функциональности.
- [x] Напишите Readme, из которого понятна функциональность проекта и инструкция по локальному запуску для разработки.
- [?] Проект должен состоять минимум из: 1 сервис с публичным API, 1 сервис с приватным API для изображений, 1 сервис СУБД, 1 сервис S3-storage.
- [x] Напишите docker-compose.yml для запуска проекта.
