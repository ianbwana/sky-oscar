# Worthwools
#### Oscar web shop

## Description
A Django web application built using the Django-Oscar e-commerce framework.

#### Requirements
1. [Python3.6](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
    - Python 3.6
    - Django-Oscar
    - Postgresql

#### Clone the Repo and enter the project folder.
```bash
git clone https://github.com/ianbwana/sky-oscar.git && cd sky-oscar
```
#### Create and activate the virtual environment
```bash
python3.6 -m venv env
```

```bash
source env/bin/activate
```

#### Create Database
Create a database on your local machine

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<secret_key>'
DB_NAME='<db name>'
DB_USER='<db username>'
DB_PASSWORD='<db password>'
DB_HOST='<db host>'
DB_PORT='<db port>'
DEBUG=<boolean>
```
#### Install dependencies
Install environmental dependencies that will enable the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

~~A hosted LIVE DEMO of this app can be found [here]~~
