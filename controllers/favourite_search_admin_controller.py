from flask import Blueprint

from init import db
from models.favourite_search import FavouriteSearch, Favourite_search_schema, Favourite_searchs_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User


favourite_search_bp = Blueprint('favourite_search_admin', __name__, url_prefix='/favourite_search_admin')

# Admin http://127.0.0.1:8080/favourite_search/2
@favourite_search_bp.route('/<int:favourite_search_id>')
@jwt_required()
def get_favourite_search(favourite_search_id):
    # check users admin status
    is_admin = is_user_admin()
    if not is_admin:
        return {"error": "you're not an admin user"}
    stmt = db.select(FavouriteSearch).filter_by(id=favourite_search_id)
    favourite_search = db.session.scalar(stmt)
    return Favourite_search_schema.dump(favourite_search)

# Admin http://127.0.0.1:8080/favourite_search
@favourite_search_bp.route('/')
@jwt_required()
def get_all_favourite_search():
    # check users admin status
    is_admin = is_user_admin()
    if not is_admin:
        return {"error": "you're not an admin user"}
    stmt = db.select(FavouriteSearch).order_by(FavouriteSearch.date_added.desc())
    favourite_searchs = db.session.scalars(stmt)
    return Favourite_searchs_schema.dump(favourite_searchs)


def is_user_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    return user.is_admin