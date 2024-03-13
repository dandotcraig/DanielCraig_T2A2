from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.account import Account
# WHY WONT THIS IMPORT
from models.favourites_list import FavouritesList
from models.search_input import SearchInput

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_tables():
    users = [
        User(
            email="admin@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            is_admin=True
        ),
        User(
            name="User 1",
            email="user1@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8')
        )
    ]

    db.session.add_all(users)

    account = [
        Account(
            account_type="business",
            user=users[0]
        ),
        Account(
            account_type="personal",
            user=users[1]
        )
    ]

    db.session.add_all(account)

    favourites_list = [
        FavouritesList(
            title=date.today(),
            account=account[0],
            search_input=search_input[0]
        )
    ]

    db.session.add_all(favourites_list)

    search_input = [
        SearchInput(
           title=date.today(),
           search_input="good places to eat in Sydney", 
           FavouritesList=favourites_list[0]
        )
    ]

    db.session.add_all(search_input)

    db.session.commit()

    print("Tables seeded")