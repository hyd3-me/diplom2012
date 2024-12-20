# Дипломный проект по специальности Python-разработчик. GB_2024
## Создание web-приложения

### Инструменты:

* Python 3.9.2
* Django 4.2.17

### Структура приложения:
- proj_fix:
главная папка проекта. включает в себя файл настройки проекта - settings.py, модуль маршрутизации проекта - urls.py, а также файл с переменными для тестирования и реализации.

- app_profile:
приложение включающее в себя логику для обработки запросов связанных с пользователями - такие как регистрация, авторизация, выход с сайта.

- app_fixgroup:
здесь реализован функционал связанный с группами - создание группы, добавление в группу
- app_controdate:
в этой части приложения происходит обработка добавления и просмотр записей о сроках годности товара.

- app_revision:
в этом модуле собран функционал связаннй с подготовкой к инвентаризации - учет записей товара на остатках по складу.

### тесты
для каждого приложения в своей директории tests находятся файлы с тестами. запуск выполняется командой:
```py
python manage.py test
```