from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ==========================
# Database Model
# ==========================
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destinations = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "destinations": self.destinations,
            "country": self.country,
            "rating": self.rating
        }


# ==========================
# Home Route
# ==========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Travel API"
    })


# ==========================
# GET All Destinations
# ==========================
@app.route("/destinations", methods=["GET"])
def get_destinations():

    destinations = Destination.query.all()

    return jsonify(
        [destination.to_dict() for destination in destinations]
    )


# ==========================
# GET Destination by ID
# ==========================
@app.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination(destination_id):

    destination = Destination.query.get(destination_id)

    if destination:
        return jsonify(destination.to_dict())

    return jsonify({
        "message": "Destination not found"
    }), 404


# ==========================
# POST Create Destination
# ==========================
@app.route("/destinations", methods=["POST"])
def create_destination():

    data = request.get_json()

    new_destination = Destination(
        destinations=data["destinations"],
        country=data["country"],
        rating=data["rating"]
    )

    db.session.add(new_destination)
    db.session.commit()

    return jsonify(new_destination.to_dict()), 201


# ==========================
# PUT Update Destination
# ==========================
@app.route("/destinations/<int:destination_id>", methods=["PUT"])
def update_destination(destination_id):

    destination = Destination.query.get(destination_id)

    if destination:

        data = request.get_json()

        destination.destinations = data["destinations"]
        destination.country = data["country"]
        destination.rating = data["rating"]

        db.session.commit()

        return jsonify(destination.to_dict())

    return jsonify({
        "message": "Destination not found"
    }), 404


# ==========================
# DELETE Destination
# ==========================
@app.route("/destinations/<int:destination_id>", methods=["DELETE"])
def delete_destination(destination_id):

    destination = Destination.query.get(destination_id)

    if destination:

        db.session.delete(destination)
        db.session.commit()

        return jsonify({
            "message": "Destination deleted successfully"
        })

    return jsonify({
        "message": "Destination not found"
    }), 404


# ==========================
# Create Database
# ==========================
with app.app_context():
    db.create_all()


# ==========================
# Run the Application
# ==========================
if __name__ == "__main__":
    app.run(debug=True)