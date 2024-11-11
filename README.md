# FAST API SAMPLE

## NOTE : add the .env file to your .gitignore, so it won't be pushed to the git repository

## Branches : 
    1 - unit testing branch : https://github.com/dkmostafa/fast-api-sample/tree/unit-testing-sample

## How to start the application : 
    1 - python3 -m venv env -- create a python enviroment 
    2 - source env/bin/activate
    3 - pip install -r requirments 
    4 - uvicorn main:app --reload
    Flask App is now running 

## Migrate Database : 
    1 - alambic init
    2 - alembic upgrade head
