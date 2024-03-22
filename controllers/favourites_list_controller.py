from flask import Blueprint, request, abort

from init import db
from models.favourites_list import FavouritesList, Favourites_list_schema, Favourites_lists_schema
from models.favourite_search import FavouriteSearch
from models.account import Account, Account_schema, Accounts_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User

favourites_list_bp = Blueprint('favourites_list', __name__, url_prefix='/account')

# Create favourite lists (auth)
# Create http://127.0.0.1:8080/account/favourites_list
@favourites_list_bp.route('/<int:account_id>/favourites_list/create', methods = ['POST'])
@jwt_required()
def create_favourites_list(account_id):
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    body_data = request.get_json()
    account = Account.query.get(account_id)
    favourites_list = FavouritesList(
        account_id = body_data.get('account_id')
    )
    db.session.add(favourites_list)
    db.session.commit()
    return Favourites_list_schema.dump(favourites_list), 201


