from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Create Database
#our API has communication with a database, so we need to create a database for our API to store data       

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db' #this is the location of our database, we are using sqlite for this project

db = SQLAlchemy(app)


#creating a model in the database which will houses the information of the database ,its like a wholes of row in the databse
# this is done through a class
#lets create a class

class destination(db.Model): #this class will be used to create a table in the database
    id = db.Column(db.Integer, primary_key=True) #this is the primary key of the table
    destination = db.Column(db.String(50),nullable = False)
    country =db.Column(db.String(50),nullable = False)
    rating = db.Column(db.Float, nullable=False)

#our model is now build up
#so now I want to convert the dataset which is inside my class destination to a JSON file for reporting,cleaning, and anylsis
#JSON is a type of data that can work with many languages ,is actually similart to python dictionaries

    def to_dict(self) :
        return {
            "id" : self.id,
            "destination" : self.destination,
            "country" : self.country,
            "rating" : self.rating
    }

#This code is creating an application context in Flask so that Flask extensions (like SQLAlchemy) know which Flask application 
# they're working with.it also help us to create the database defined by the methods
with app.app_context():
    db.create_all() #This tells SQLAlchemy:"Create all the database tables that are defined by my models.


#Create routes
# a route is something like https://www.google.com/ or https://www.youtube.com/
@app.route('/')    # a home page is defined by the '/' route
def home():
    return "Hello, World!" # this will be displayed on the home page



#this will constanly keep our app running and will be used to run the app
if __name__ == '__main__':
    app.run(debug=True)
