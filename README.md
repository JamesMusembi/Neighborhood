# Neighborhood
Neighborhood is a site whereby one can upload their hood and they can get updates of latest news of their estates also they can view business around

#### Technologies used
    - Python 3.9
    - HTML
    - Bootstrap 3
    - Heroku
    - Postgresql
    - Django, Django Rest Framework

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
NAME='awward'
USER='<Username>'
PASSWORD='<password>'
HOST='localhost'
MODE='dev'
DEBUG=True
DISABLE_COLLECTSTATIC=1
```
#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE awward;
```

#### Make and run migrations
```bash
python3.9 manage.py makemigrations && python3.9 manage.py migrate
```

#### Run the app
```bash
python3.9 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

## Running the tests

Run test using the following command


```
 ./manage.py test hood
```

## Authors

* **James Musembi** - [JamesMusembi](https://github.com/JamesMusembi)


* **Clinton Wambugu** - [Clinton-dev](https://github.com/Clinton-dev)


### License
MIT
Copyright (c)2022 **James Musembi**