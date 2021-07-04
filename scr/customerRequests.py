from books import *

class CustomerRequest(db.Model):
    __tablename__ = "custRequests"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(100))
    bookId = db.Column(db.Integer, db.ForeignKey('books.id'))
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return pretty_result(code.DB_ERROR, 'Please check the Database server')
        else:
            return self
    def __init__(self,name,phone,address,bookId):
        self.name = name
        self.phone = phone
        self.address = address
        self.bookId = bookId
    def __repr__(self):
        return '' % self.id