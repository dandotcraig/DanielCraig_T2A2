from flask import Blueprint, request

from init import db
from models.favourites_list import FavouritesList, Favourites_list_schema, Favourites_lists_schema
from models.favourite_search import FavouriteSearch
from models.account import Account, Account_schema, Accounts_schema
from flask_jwt_extended import jwt_required

favourites_list_admin_bp = Blueprint('favourites_list_admin', __name__, url_prefix='/favourites_list')

# Get ALL favourite lists (auth)
# Admin http://127.0.0.1:8080/account/favourites_list
@favourites_list_admin_bp.route('/')
@jwt_required()
def get_all_favourites_list():
    stmt = db.select(FavouritesList).order_by(FavouritesList.date_added.desc())
    favourites_list = db.session.scalars(stmt)
    return Favourites_lists_schema.dump(favourites_list)