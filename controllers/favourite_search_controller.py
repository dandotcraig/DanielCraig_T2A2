from flask import Blueprint, request
from init import db
from models.favourite_search import FavouriteSearch, Favourite_search_schema, Favourite_searchs_schema
from models.favourites_list import FavouritesList, Favourites_list_schema
from models.account import Account, Account_schema, Accounts_schema
from models.search_input import SearchInput, Search_input_Schema, Search_inputs_Schema
from flask_jwt_extended import jwt_required, get_jwt_identity

favourite_search_bp = Blueprint('favourite_search', __name__, url_prefix='/account')

# Delete accounts favourites search
# Delete http://127.0.0.1:8080/account/2/favourites_list/2
@favourite_search_bp.route('/<int:account_id>/favourites_list/<int:favourites_list_id>', methods=['DELETE'])
@jwt_required()
def delete_favourite_search(favourite_search_id, account_id):
    favourite_search = db.session.query(FavouriteSearch).filter_by(id=favourite_search_id).first()
    if favourite_search:
        db.session.delete(favourite_search)
        db.session.commit()
        return {"message": f"Favourite search with id {favourite_search_id} has been deleted"}
    else:
        return {"error": f"Favourite search with id {favourite_search_id} not found"}, 404
    
# Create accounts favourites search Clicks on a search input, while already logged in
# Create http://127.0.0.1:8080/account/2/favourites_list/
@favourite_search_bp.route('/<int:account_id>/favourites_list/<int:favourites_list_id>', methods=['POST'])
@jwt_required()
def create_favourite_search(account_id, favourites_list_id):
    body_data = request.get_json()
    stmt = db.select(FavouritesList).filter_by(id=favourites_list_id)
    favourites_list = db.session.scalar(stmt)
    if favourites_list:
        favourite_search = FavouriteSearch(
            search_input_id = body_data.get('search_input_id'),
            favourites_list_id = favourites_list_id
        )
        db.session.add(favourite_search)
        db.session.commit()
        return Favourite_search_schema.dump(favourite_search), 201
    else:
        return {"error": f"Favourites list with id {favourites_list_id} doesn't exist"}, 404
    