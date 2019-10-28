### A simple meeting room booking app
### 회의실 예약 서비스


## virtual environment
create a virtual environment called `venv` (you can use any other names)
```
python3 -m venv venv
```

must activate virtual environment before doing anything. especially before installing pip packages.
```
. venv/bin/activate
```

## pip

install package
```
pip install `package name`
eg) pip install numpy
```

when you want to freeze pip packages into requirements.txt <br> 
(pip 로 install한 패키지 리스트를 requirements.txt 에 나열하고 싶을 때 requirements.txt가 있는 경로에서 아래 커맨드를 실행한다)
```
pip freeze > requirements.txt
```

when you want to install all packages from requirements.txt
```
pip install -r requirements.txt
```


## Database : postgre

install postgre
```
brew install postgresql
```

check version
```
postgres -V
```

create database called `bookameeting`
```
CREATE DATABASE bookameeting;
```

Create role with `bookameeting`
```
CREATE ROLE bookameeting WITH LOGIN PASSWORD 'bookameeting';
```

grant prvileges to database `bookameeting` with user `bookameeting`
```
GRANT ALL PRIVILEGES ON DATABASE bookameeting TO bookameeting;
```

alter role
```
ALTER USER bookameeting CREATEDB;
```

connect to `bookameeting` database with user `bookameeting`
```
psql bookameeting -U bookameeting
```