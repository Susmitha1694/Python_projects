from customerRequestSchema import *
#creates all the schema and the tables
db.create_all()

#add some initial books to the database
#book1 = Book("A thousand Splendid suns","Khaled Hosseine","drama","It is about two friends")
#book2 = Book("The Secret","Rhonda Byrne","self-help","Key to success")
#db.session.add(book1)
#db.session.add(book2)
#db.session.commit()

#get a list of all the avaiable books
@app.route('/books', methods = ['GET'])
def get_books():
    get_books = Book.query.all()
    book_schema = BookSchema(many=True)
    books = book_schema.dump(get_books)
    return make_response(jsonify({"book": books}))
#get the details of a specific book by id
@app.route('/books/<id>', methods = ['GET'])
def get_book_by_id(id):
    try:
        get_book = Book.query.get(id)
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return pretty_result(code.DB_ERROR, 'could not find the book and check the server')
    else:
        book_schema = BookSchema()
        book = book_schema.dump(get_book)
        return make_response(jsonify({"book": book}))
#get a list of all the avaiable books
@app.route('/books/requests', methods = ['GET'])
def get_requests():
    get_books = CustomerRequest.query.all()
    customer_request_schema = CustomerRequestSchema(many=True)
    customer_requests = customer_request_schema.dump(get_books)
    return make_response(jsonify({"requests": customer_requests}))
#take the request for a book from a user
@app.route('/books/requests', methods = ['POST'])
def create_customer_request():
    data = request.get_json()
    customer_request_schema = CustomerRequestSchema()
    result = []
    for i in data:
        customer_request = customer_request_schema.load(i)
        result.append(customer_request_schema.dump(customer_request.create()))
    return make_response(jsonify({"request": result}),200)
#add a new book to the database
@app.route('/books', methods = ['POST'])
def create_book():
    data = request.get_json()
    book_schema = BookSchema()
    book = book_schema.load(data)
    result = book_schema.dump(book.create())
    return make_response(jsonify({"request": result}),200)

if __name__ == "__main__":
    app.run(debug=True,port=8080,host='0.0.0.0')





































