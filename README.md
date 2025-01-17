# API YaMDb

API YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».

## Описание

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

### Возможности API
- Создание и управление отзывами на произведения
- Комментирование отзывов
- Оценка произведений по шкале от 1 до 10
- Категоризация произведений
- Жанровая классификация
- Система ролей пользователей

## Роли пользователей

- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь** — может читать всё, писать отзывы и ставить оценки произведениям, комментировать отзывы.
- **Модератор** — те же права, что и у аутентифицированного пользователя плюс право удалять и редактировать любые отзывы и комментарии.
- **Администратор** — полные права на управление всем контентом проекта.

## Технологии
- Python 3
- Django REST Framework
- Simple JWT для аутентификации

## Как запустить проект

1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/your-username/api_yamdb.git
cd api_yamdb
```

2. Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

4. Выполнить миграции:
```
python manage.py migrate
```

5. Запустить проект:
```
python manage.py runserver
```

## Документация API
Документация доступна по эндпоинту: http://127.0.0.1:8000/redoc/

## Автор
Теняков Денис
Василий Скороход
Ирина Барман