# Airbnb Clone

Cloning Airbnb with Python, Django, Tailwind and more... 🇰🇷💖🐍

pipenv 실행하기: pipenv shell
장고 위치 확인: which django-admin

장고를 시작하기위한 명령어
ex1) 
    cd Document
    pipenv shell
    django-admin startproject mysite

ex2)
    cd Document
    mkdir mysite
    cd mysite
    django-admin startproject config
    rename config -> Aconfig
    move to Aconfig/* ~/
    rm -rf Aconfig


linter, formatter설치
linter: pipenv install flake8 --dev
formatter: pipenv install black --dev --pre

파이썬 서버 실행
    pipenv shell
    pythone manage.py runserver

DB table magrate
    python manage.py migrate

관리자 계정 생성
    python manage.py createsuperuser
    계정명, email, 비밀번호 입력 후 생성.
    