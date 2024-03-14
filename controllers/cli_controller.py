from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.account import Account
# WHY WONT THIS IMPORT
from models.favourites_list import FavouritesList
from models.search_input import SearchInput
from models.favourite_search import FavouriteSearch

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
    db.session.commit()


    accounts = [
        Account(
            account_type="business",
            users=[users[0]]
        ),
        Account(
            account_type="personal",
            users=[users[1]]
        )
    ]

    db.session.add_all(accounts)
    db.session.commit()


    favourites_lists = [
        FavouritesList(
            date=date.today(),
            account=accounts[0],
            search_input=search_inputs[0]
        ),
        FavouritesList(
            date=date.today(),
            account=accounts[1],
            search_input=search_inputs[1]
        )
]


    db.session.add_all(favourites_lists)
    db.session.commit()


    search_inputs = [
        SearchInput(
            date=date.today(),
            search_input="good places to eat in Sydney",
            favourites_list=favourites_lists[0]
        ),
        SearchInput(
            date=date.today(),
            search_input="cafe Sydney",
            favourites_list=favourites_lists[1]
        )
    ]

    db.session.add_all(search_inputs)
    db.session.commit()


    favourite_searches = [
        FavouriteSearch(
            search_input=search_inputs[0],
            favourites_list=favourites_lists[0]
        )
    ]

    db.session.add_all(favourite_searches)
    db.session.commit()

    print("Tables seeded")
