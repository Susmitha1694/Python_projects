import sys
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
username = sys.argv[1]
password = sys.argv[2]
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+username+':'+password+'@localhost:3306/library'
db = SQLAlchemy(app)

###Models####
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    genre = db.Column(db.String(20))
    description = db.Column(db.String(100))
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return pretty_result(code.DB_ERROR, 'Please check the Database server')
        else:
            return self
    def __init__(self,title,author,genre,description):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
    def __repr__(self):
        return '' % self.id