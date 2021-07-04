This application uses mysql as the database and pymysql driver.
We need to create a library database before execution.
use the following command in the workbench or sql command line:
	"create database library"

Run command for the file requires the usename and password of mysql to be provided in the arguments 
(all the python files must be in the same directory and navigate to the folder before executing the command):
	"python library_api.py <mysql username> <mysql password>"

Please run these commands to insert few data into books table:
insert into books(title,author,genre,description) values('A thousand Splendid suns','Khaled Hosseine','drama','It is about two friends');
insert into books(title,author,genre,description) values('The Secret','Rhonda Byrne','self-help','Key to success');

create a virtual environment using the command python -m venv <name_of_virtual_env>

then activate the virtual environment

install the requirements "pip install -r src\requirements.txt"

There are overall 5 files as follows:
	books.py - has all the initial imports and book model class
	bookSchema.py - as the name suggests it has the schema for the book model
	customerRequest.py - the request for borrowing the books is modeled by this class
	customerRequestSchema.py - the schema for customerRequest model
	library_api.py - main file that contains all the url mappings.

The app is configured to run on host: 0.0.0.0 and port: 8080

we can use the postman app to test the endpoints.

This application provides 4 end points:
	Purpose: Used to get details of all the books that are present
	URL: /books
	Method: GET
	Result: all the books that are listed in the database
	
	Purpose: Used to get details of only one book with a specific id
	URL: /books/{id}
	Method: GET
	Result: Book details that has the id 
	
	Purpose: 
	URL: /books
	Method: POST
	request:
	{
		"author": "Khaled Hosseine",
		"description": "It is about two friends",
		"genre": "drama",
		"title": "A thousand Splendid suns"
	}
	result: The request with the id and if error it will give the error.
	
	Purpose: Takes request to borrow books
	URL: /books/requests
	Method: POST
	request:
	[
		{
		"name": "krishnaveni",
		"phone": "87655439",
		"address": "no 4, plot 7, brindavanam, DY45TR",
		"bookId": "1"
		},
		{
		"name": "krishnaveni",
		"phone": "87655439",
		"address": "no 4, plot 7, brindavanam, DY45TR",
		"bookId": "2"
		}
	]
	
Here I have considered that the user will view all the avaiable books and select which ever book they want.
Thus the borrow request will contain the user details and book id's they want to borrow.