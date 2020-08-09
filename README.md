# Django Project Test

In this project there two models User and Activityperiod and also custom management command which will populate the database. 


### 1. Clone the application

Install [git](https://git-scm.com/downloads) and [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
Run a terminal (or console) on your machine and type

```
git clone https://github.com/sushilr007/Fullthrottle_App.git
cd Fullthrottle_App
conda create --name env
conda activate env
pip install -r requirements.txt
heroku login
heroku create 
git add .
git commit -m "Commit message"
git push heroku master
heroku run bash 
python manage.py migrate
python manage.py runserver
```

## To run locally
```
cd Fullthrottle_App/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Go to browser at paste URL where the server is running

## API Endpoint 
There are two user id added in database.

W07QCRPA4 and W012A3CDE. 

https://pure-dawn-09272.herokuapp.com/get_user_info/user/<USER_ID>/
