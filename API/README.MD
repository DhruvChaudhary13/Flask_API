# Flask API for App Management

This is a basic Flask API to manage app details, allowing you to add, retrieve, and delete app information.

## Setup Instructions

3. **Install dependencies**:

4. **Initialize the database**:
Before running the app, create the database by running the following in a Python shell:


## from app import db
##  db.create_all() 



**fILES**

1. __init__.py   # it is to initialise the flask app
2.models.py      # contain the structure of the database 
3.rotes.py       # paths defined to send and handle the request

## URL

**http://127.0.0.1:5000/add-data** url to add data to server
**http://127.0.0.1:5000/get-app/<int:id>** url to get the data based on id which is a  primary key
**http://127.0.0.1:5000/delete-app/<int:id>** url  to delete a particular entry based on primary key or id





5 **Run the application**:
 run.py  ## it is the file which  is to be run to starts the server 

