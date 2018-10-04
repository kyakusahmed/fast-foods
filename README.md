[![Build Status](https://travis-ci.org/kyakusahmed/fast-foods.svg?branch=CHALLENGE-3)](https://travis-ci.org/kyakusahmed/fast-foods)
[![Coverage Status](https://coveralls.io/repos/github/kyakusahmed/fast-foods/badge.svg?branch=CHALLENGE-3)](https://coveralls.io/github/kyakusahmed/fast-foods?branch=CHALLENGE-3)
[![Maintainability](https://api.codeclimate.com/v1/badges/d0de8b9e4f09f978e53e/maintainability)](https://codeclimate.com/github/kyakusahmed/fast-foods/maintainability)

## Fast-Food-Fast Application.

Food delivery service app for a restaurant 

[GH-PAGES](https://kyakusahmed.github.io/fast-foods/UI/)

### How to run the app


Make sure that python 3.4/3.5/3.6/3.7 is installed on your computer

Clone the repo
```
git clone https://github.com/kyakusahmed/fast-foods.git
```
Change to the app directory
```
$ cd fast-foods
```
Create a virtual enviroment
```
virtualenv (name)
```
Activate the virtualenv
```
For Windows:
	$ (virtualenv name)\scripts\activate, and  	
For Linux: 
 	$source(virtualenv name)/bin/activate
```
Install the required modules from the requirements.txt file 
```
$ pip install -r requirements.txt
```
Run the app
```
$ python run.py
```

### Heroku link
https://ahmad-fast-food-fast.herokuapp.com/api/v1/orders

| tasks               |    URLS                |  METHOD  |         PARAMS              | 
| ------------------- | -----------------------|----------|-----------------------------|
| get all orders      | api/v1/orders          |  GET     |   ---------------           |
| get aspecific order | api/v1/orders/id       |  GET     |   ---------------           |
| post an order       | api/v1/orders          |  POST    | foodid, userid, date, status| 
| update the status   | api/v1/orders/id       |  PUT     | status                      |
|                     |                        |          |                             |
	
### How to run the Tests:

 open the terminal,activate virtual enviroment in the fast-foods directory  and enter:
 ```
 $ pytest
```
 using nosetest  in open the terminal,activate virtual enviroment in the fast-foods directory and enter:
 ```
 $ nosetests --with-coverage --cover-tests
 ```

