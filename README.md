# Marketplace_Pycharm

## Description
Marketplace project example for python (django)

## Onboarding and Development Guide
### Prerequisites
- Python3 3.7.7 (Primary)
- GIT

### Setup and Installation
#### Linux
```
$ sudo apt-get update
$ sudo apt-get install python3.6
$ sudo dnf install python3
```
#### Mac
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ export PATH="/usr/local/opt/python/libexec/bin:$PATH" (Latest OS X)
$ export PATH=/usr/local/bin:/usr/local/sbin:$PATH (OS X 10.12 (Sierra) or older)
$ brew install python
```
#### Setup Project
```
$ python3 -V
$ pip install --upgrade pip
$ git clone git@github.com:rizkypascal/marketplace_pycharm.git
$ cd marketplace_pycharm
$ python3 -m venv env
$ . env/bin/activate
$ cp env.sample .env
$ pip install -r requirements.txt
$ pip manage.py makemigrations
$ pip manage.py migrate
```
#### Run Project
```
$ python3 manage.py runserver <port>
```
#### Run Unit Test
```
$ pip install factory_boy
$ python3 manage.py test apps.<dir>
```
#### Console
```
$ python3 manage.py shell
```

## Future Developments
1. Use PostgreSQL
2. Apply coverage testing (unit tests are exist but not reporting to coverage)
3. Find another alternative for Factory in order to compatible with Python3