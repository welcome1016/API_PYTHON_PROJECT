from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)





#this will constanly keep our app running and will be used to run the app
if __name__ == '__main__':
    app.run(debug=True)
