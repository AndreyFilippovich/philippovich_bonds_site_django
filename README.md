# philippovich_bonds_site_django


## Снача устанавливаем venv:

- python -m venv venv

## Активируем виртуальное окружение:

- source venv/scripts/activate

## Переходим в папку проекта:

- cd philippovich_bonds_site_django

## Устанавливаем зависимости:

- pip install -r requirements.txt

## Скачиваем статику:

- python manage.py collectstatic

## Устанавливаем миграции:

- python manage.py migrate

## Запускам проект:

- python manage.py runserver