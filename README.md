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

1개의 프로젝트에는 1개이상의 application이 존재한다.
1개의 application은 1개의 문장으로 표현가능하다.(and가 들어간다면, 2개의 application으로 쪼개는걸 고민)
ex) user - 로그인, 로그아웃, 계정생성, 상세보기 && 메시지 보내기 <-- 분리.

application 생명 명령어(단, appName은 반드시 복수로 표현)
    django-admin startapp appName

model변경 후 명령어
1) 변경된 모델을 django에서 인식하기 위하여 makemigrations명령을 실행.
    python manage.py makemigrations

2) 적용된 migrate를 db에 적용하기 위한 migrate명령어 실행.
    python manage.py migrate

 ☀︎ 사용자 테이블을 삭제한경우 createsuperuser명령어로 admin계정을 생성해 줘야됨.

사용자 테이블 확장
user.model.py

새로운 컬럼 추가
null=True/False: DB에 값을 설정.
blank=True/False: admin페이지에서 필수값 여부 설정.
choices: 원하는 값만 선택할 수 있도록 설정.


models(Table mapper) 추가 --> 관리자 페이지에서 관리한 model맵핑
models-admin 맵핑 방법
1) 데코레이터
    ex)
    @admin.register(models.모델명)

2) 직접등록
    ex)
    dmin.site.register(models.모델명, 실제맵핑할모델명)

공통 application생성
이유: 공통 기능, 모델을 확장하여 다른 어플리케이션에서 사용할 수 있도록 하기 위하여 공통 application생성.
1) core Application생성.
django-admin startapp core

