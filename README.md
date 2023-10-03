# philippovich_bonds_site_django

Мой личный сайт со статьями по инвестиционной тематике. Сделан в удобной форме, чтобы уроки шли один за другим.

### Технологии:
![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat&logo=css3&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=flat&logo=bootstrap&logoColor=white) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white) ![JWT](https://img.shields.io/badge/JWT-black?style=flat&logo=JSON%20web%20tokens) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=flat&logo=sqlite&logoColor=white)


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
