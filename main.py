from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Create Database
#our API has communication with a database, so we need to create a database for our API to store data       

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db' #this is the location of our database, we are using sqlite for this project

db = SQLAlchemy(app)



#Create routes
# a route is something like https://www.google.com/ or https://www.youtube.com/
@app.route('/')    # a home page is defined by the '/' route
def home():
    return "Hello, World!" # this will be displayed on the home page



#this will constanly keep our app running and will be used to run the app
if __name__ == '__main__':
    app.run(debug=True)
