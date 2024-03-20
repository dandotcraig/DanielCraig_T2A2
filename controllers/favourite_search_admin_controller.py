from flask import Blueprint

from init import db
from models.favourite_search import FavouriteSearch, Favourite_search_schema, Favourite_searchs_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


favourite_search_bp = Blueprint('favourite_search_admin', __name__, url_prefix='/favourite_search_admin')

# HIDDEN http://127.0.0.1:8080/favourite_search/2
@favourite_search_bp.route('/<int:favourite_search_id>')
def get_favourite_search(favourite_search_id):
    stmt = db.select(FavouriteSearch).filter_by(id=favourite_search_id)
    favourite_search = db.session.scalar(stmt)
    return Favourite_search_schema.dump(favourite_search)

# HIDEN http://127.0.0.1:8080/favourite_search
@favourite_search_bp.route('/')
@jwt_required()
def get_all_favourite_search():
    stmt = db.select(FavouriteSearch).order_by(FavouriteSearch.date_added.desc())
    favourite_searchs = db.session.scalars(stmt)
    return Favourite_searchs_schema.dump(favourite_searchs)