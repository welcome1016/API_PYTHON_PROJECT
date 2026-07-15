from flask import Flask, jsonify, request
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
    destinations = db.Column(db.String(50),nullable = False)
    country =db.Column(db.String(50),nullable = False)
    rating = db.Column(db.Float, nullable=False)

#our model is now build up
#so now I want to convert the dataset which is inside my class destination to a JSON file for reporting,cleaning, and anylsis
#JSON is a type of data that can work with many languages ,is actually similart to python dictionaries

    def to_dict(self) :
        return {
            "id" : self.id,
            "destinations" : self.destinations,
            "country" : self.country,
            "rating" : self.rating
    }

#This code is creating an application context in Flask so that Flask extensions (like SQLAlchemy) know which Flask application 
# they're working with.it also help us to create the database defined by the methods
with app.app_context():
    db.create_all() #This tells SQLAlchemy:"Create all the database tables that are defined by my models.


#Create routes
# a route is something like 
 #https://www.thenerdnook.io/
@app.route('/')    # a home page is defined by the '/' route
def home():
    return jsonify({"message": "welcome to the Travel API"}) # this will be displayed on the home page


 #https://www.thenerdnook.io/destinations ,destination is an extender
#we want to return all the destinations we have sent to our API that are in our database
@app.route("/destinations", methods =["GET"])
def get_destinations() :
    destinations = destinations.query.all()

    return jsonify([destinations.to_dict()] for destination in destinations)


#https://www.thenerdnook.io/destinations/2 we're looking for ID 2 now
@app.route("/destinations/<int:destination_id>", methods = ["GET"]) #this will constanly keep our app running and will be used to run the app
def get_destination(destination_id) :
    destination = destination.query.get(destination_id) 
    if destination:
        return jsonify(destination.to_dict())
    else:
        return jsonify({"message": "Destination not found"}), 404

#POST

    data = request.get_json() #this will get the data from the request body
    new_destination = destination(
        destinations = data["destinations"],
        country = data["country"],
        rating = data["rating"]
    )
    db.session.add(new_destination) #this will add the new destination to the database
    db.session.commit() #this will commit the changes to the database
    return jsonify(new_destination.to_dict()), 201 #this will return the new destination as a JSON object with a 201 status code

#PUT it means apdate something , here will will apdate by ID
@app.route("/destinations/<int:destination_id>", methods = ["PUT"])
def update_destination(destination_id) :
    destination = destination.query.get(destination_id)
    if destination:
        data = request.get_json()
        destination.destinations = data["destinations"]
        destination.country = data["country"]
        destination.rating = data["rating"]
        db.session.commit()
        return jsonify(destination.to_dict())
    else:
        return jsonify({"message": "Destination not found"}), 404




if __name__ == '__main__':
    app.run(debug=True)
