# Использование Docker в приложении Flask с БД

## Задание

На основе файлов [проекта с приложением-счетчиком на Flask](https://gist.github.com/nzhukov/a2ba90e8d801e66d1319ee2bf962bc28), продемонстрированного на прошлом занятии, реализовать развертывание приложения-счетчика, реализованного в предыдущем задании с использованием с одной из следующих СУБД: Mongo, PostgreSQL, MySQL / Maria DB с использованием Docker Compose.
В базе данных должно храниться не только значение счетчика, но и данные о том, когда запрос был сделан (для того, чтобы использовать эту информацию в дальнейшем).

В отчёте по заданию представить ссылку на репозиторий в гитхаб с содержимым каталога c Dockerfile, docker-compose.yml и другими необходимыми для развертывания файла. Если решение загружено на hub.docker.com, то также ссылку на образ. В отчете отразить последовательность действий, необходимую для развертывания решения.

## Инструкиця по развертыванию

##### 1. Клонируем репозиторий

```bash
git clone <rep_id>
```

##### 2. Развёртываем сервисы веб-приложений и создаём из docker-образов новые контейнеры

```bash
docker-compose up --build
```

###### 2.1 Если образы уже есть

Достаточно `docker-compose start`

##### 3. Проверяем работу

- Переходим по адресу `http://localhost:8080`
- При каждом обновлении страницы будут появляться новые посещения страницы
- Данные будут отображаться в формате JSON
