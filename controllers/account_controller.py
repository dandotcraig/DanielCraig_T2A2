from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.account import Account, Account_schema, Accounts_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.favourites_list import FavouritesList, Favourites_list_schema, Favourites_lists_schema





account_bp = Blueprint('account', __name__, url_prefix='/account')

# Get accounts favourites_list
# http://127.0.0.1:8080/account/2/favourites_list
@account_bp.route('/<int:account_id>/favourites_list')
@jwt_required()
def get_favourites_list(account_id):
    stmt = db.select(FavouritesList).filter_by(id=account_id)
    favourites_list = db.session.scalar(stmt)
    if favourites_list:
        return Favourites_list_schema.dump(favourites_list)
    else:
        return {"ERROR": f"Favourite with this account {account_id} not found"}, 404

# http://127.0.0.1:8080/account/2
@account_bp.route('/<int:account_id>')
@jwt_required()
def get_account(account_id):
    stmt = db.select(Account).filter_by(id=account_id)
    account = db.session.scalar(stmt)
    if account:
        return Account_schema.dump(account)
    else:
        return {"ERROR": f"Account with {account_id} not found"}, 404

# Get ALL accounts (auth)
# ADMIN http://127.0.0.1:8080/account
@account_bp.route('/')
@jwt_required()
def get_all_accounts():
    stmt = db.select(Account).order_by(Account.date_added.desc())
    accounts = db.session.scalars(stmt)
    return Accounts_schema.dump(accounts)

# Create account (auth)
# CREATE http://127.0.0.1:8080/account
@account_bp.route('/', methods=['POST'])
@jwt_required()
def create_account():
    body_data = request.get_json()
    # Create new card
    account = Account(
        is_business_account = body_data.get('is_business_account'),
        user_id = get_jwt_identity()
    )
    # Add to session
    db.session.add(account)
    db.session.commit()

    return Account_schema.dump(account), 201

# DELETE http://127.0.0.1:8080/account
@account_bp.route('/<int:account_id>', methods=['DELETE'])
@jwt_required()
def delete_account(account_id):
    stmt = db.select(Account).where(Account.id == account_id)
    account = db.session.scalar(stmt)
    # Add to session
    if account: 
        db.session.delete(account)
        db.session.commit()
        return {'message': f"{account.id} deleted successfully"}
    
    else:
        return {'error': f"account with id {account_id} not found"}, 404
