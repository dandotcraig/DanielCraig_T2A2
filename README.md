# ASSESSMENT: API WEBSERVER PROJECT
## R1	
### Identification of the problem you are trying to solve by building this particular app.
---
Insight: Anytime you want to find a real answer on google, you get thousands of SEO optimised pages of garbage. On the other hand, reddit is full of great real suggestions which are validated by real people and tend to have the answer you’re looking for. 

Problem: Google's search results and searching on reddit is bad. Combine them together solves the problem. Simply {what you want want to search} + “site:www.reddit.com” (for some reason it yields better results than just adding ‘reddit’ to your search).

## R2	
### Why is it a problem that needs solving?
---
Users online require good information. Due to people SEO experts gaming the system, users are served more and more optimised articles which don't lead users to valid information. With the rise of AI, Google's search engine is destin to be come a garbage pit of rubbish articles. If I google 'Best resturants sydney' top search is '65 best restaurants in Sydney you should be booking' this is clearly SEO optimised, full of advertising and potentially the 65 resturants could have paid to be apart of it. If I type 'best sydney restaurants site:www.reddit.com' I get a reddit article titled 'Must Eats in Sydney?' with 605 comments and the top comment voted to the top by 492 people. It's also only 4 months old, so its relivant too!

## 3	
### Why have you chosen this database system. What are the drawbacks compared to others?
---
For this project I will be using PostgreSQL. PostgreSQL is an open-source advanced database. Its a great database as it can be configired in relational and non relational ways. Its extremely stable and has been around for more than 20 years. PostgreSQL use the Structured Query Language which is a way of joining and querying tables. PostgreSQL is a Object-Relational Database Management System which simply means it merged the best of both worlds relational and object-oriented structures. Its great for reading and writing information.

PostgreSQL is a great choice as it connects with Python via Flask easily. PostgreSQL is a great database for projects which require future scalability and its wildly use for projects which require the need for fast scale growth.

PostgreSQL is full of features which is why its perfect for a large range of applications. I can work with many programing languages, it can storage a range large binary objects as well as range of attributes which can streamline any projects database like Foreign keys and triggers. PostgreSQL has a vastaray of data types in which is supports which is important for projects which are forever growing.

PosgreSQL is often compared to another open-source database MySQL. Similarly to PostgreSQL its a Structured Query Language. MySQL is famous for being apart of the LAMP stack, which is an acronym for a tech stack which was developed in the late 1990s. This stack is famous due to the fact a lot of the internet still runs on this and that its all open-source. Due to this factor, MySQL has a massive community of experts and supports many platforms. MySQL is a relational database management system. If you were looking for a database to manage read-only commands, MySQL is perfect.

Other common databases are MongoDB. Oracle & SQLite to name a few.

PostgreSQL was the easy choice in this situation as for future requirements I see the ability to read and write and the need for large databases being a factor. There is a large community of support as well, where I can essentially get any question anwswered, PostgreSQL is the clear winner.

## R4	
### Identify and discuss the key functionalities and benefits of an ORM
---
Object Relational Mapping is the process of writing interactions with a choosen relational database into the code itself. For example, its using Python and SQL together but the ORM is the bridge between the two. This means that rather than using plain SQL code we are intergrating it into our original code. To create this bridge for python on SQL, SQLAlchemy would be employed to get the job done.

The key functions of an ORM include:
* Simplifies the process quering the database, by generating methods
* Can apply the following actions to a database: creates, reads, updates and deletes AKA CRUD
* Maps the Ojects relationships

Key benefits include:
* Simplification of SQL code, while also being clearer and easy to understand
* Easier to implement changes and updates

Drawbacks include:
* Can be time consuming to install
* Understanding of both databases and SQL is required

## R5	
### Document all endpoints for your API
---

ADD IN ANY 404,201 etc - expected response

### CREATE user /auth/register
Request:
```json
{
	"name": "User 5",
	"email": "user5@email.com",
	"password": "123456"
}
```
Response:
```json
{
	"id": 1,
	"name": "User 1",
	"email": "user1@email.com",
	"is_admin": false,
	"cards": []
}
```
---
### GET user login /auth/login
Request:
```json
{
	"email": "admin@email.com",
	"password": "123456"
}
```
Response:
```json
{
	"email": "admin@email.com",
	"token": "",
	"is_admin": true
}
```

or for users

```json
{
	"email": "user1@email.com",
	"token": "",
	"is_admin": false
}
```
---
### (external) POST Search /searches
Request:
```json
{
	"search": "",
	"date": "00/00/00"
}
```
Response:
```json
{
	"id": 1,
	"search": "",
	"date": "00/00/00"
}
```
---
### GET all search results /searches
Response:
```json
{
	"id": 1,
	"search": "",
	"date": "00/00/00"
}
```
---
### GET Favourites /users/{user_id}/favorites
Response:

User would get all favourites in there current list
```json
{
	"id": 1,
	"search": "",
	"date": "00/00/00"
}
```
---
### POST Favourite /users/{user_id}/favorites
Request:
```json
{
	"id": 1,
}
```
Response:

User would recieve all favourites which have been added to their favourites list.
```json
{
	"id": 1,
	"search": "",
	"date": "00/00/00"
}
```
---
### DELETE Favourite /users/{user_id}/favorite/{favourite_id}
Request:
```json
{
	"id": 1,
}
```
Response:

User would recieve all favourites which have been deleted to their favourites list.
```json
{
	"id": 1,
	"search": "",
	"date": "00/00/00"
}
```
---


## R6	
### An ERD for your app
---
UPDATE 
![ERD](<img/Screenshot 2024-03-06 at 6.59.14 am.png>)
## R7	
### Detail any third party services that your app will use
---
Flask:
* flask_sqlalchemy - 
* flask_marshmallow -
* flask_bcrypt import -
* flask_jwt_extended -
* datetime -


## R8	
### Describe your projects models in terms of the relationships they have with each other
---
For this project we are utilizing four models. These models include search_input, favourite_list, account and user.

Search_input takes search inputs from the websites front end. It numbers them and adds a date to them. Its then collected in order of recieved and kept in this database. Its primary is search_input_id and it has a many to many relationship with the favourite list, this is due to there being many searchs added that can be added to many favourite lists. Its attributes include search_input, search_input_id, number & date.

Favourite list is a list where our logged in (SEO expert user) can save their favourite and most insightful searchs to a favourite list to use with in their work. It accepts a foreign key from search_input_id in order to save the favourited search result to the search list. It has a primary key favourite_list_id. This relationship between account and favourite list is one to one as, only one user can have one favourite list. Its attributes include favourite_list_id, search_input_id & date added,

The account model has four attributes, account_id, user_id, favourite_list_id and account type. Acount_id is the primary key and it accepts two foreign keys, user_id and favourite_list_id which joins it to both the favourite_list model and the user_id model. It has an account type as some users might be businesses and some might be regular users. This then means the relationship between account and user is one to many, as a business can have many users.

The user model is simple with a name, email and password.

## R9	
### Discuss the database relations to be implemented in your application
---
One to one:
* each user can have only one favourite list

one to many:
* many searches can be added to many search lists
* many accounts can have many users

## R10	
### Describe the way tasks are allocated and tracked in your project
---
All tasks will be allocated and tracked using the free version of Trello. First each task will be added to a card requirements and dates. They will sit in an adgile work flow collumns where they will be allocated within the work flow. This means when a task is being worked on it will sit int the working column, once its complete it will be moved to the complete column.

## Reference
* https://aws.amazon.com/rds/postgresql/what-is-postgresql/
* https://www.integrate.io/blog/postgresql-vs-mysql-which-one-is-better-for-your-use-case/#:~:text=MySQL%20is%20preferred%20for%20managing,preferred%20for%20read%2Donly%20operations.
* https://kinsta.com/blog/postgresql-vs-mysql/#:~:text=Ultimately%2C%20it%20comes%20down%20to,massive%20datasets%2C%20and%20complicated%20queries.
* https://kinsta.com/blog/postgresql-vs-mysql/#:~:text=Ultimately%2C%20it%20comes%20down%20to,massive%20datasets%2C%20and%20complicated%20queries.
* https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/
* https://stackoverflow.com/questions/2676133/best-way-to-do-enum-in-sqlalchemy
* https://medium.com/@danielwume/must-know-package-to-build-your-system-real-world-examples-with-sqlalchemy-in-python-db8c72a0f6c1
* https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-one
* https://rest-apis-flask.teclado.com/docs/sqlalchemy_many_to_many/many_to_many_relationships/
* https://stackoverflow.com/questions/18110033/getting-first-row-from-sqlalchemy
* https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html
* https://stackoverflow.com/questions/61051249/what-exactly-is-the-attribute-in-marshmallow-fields-nested-function