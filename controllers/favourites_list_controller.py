from flask import Blueprint

from init import db
from models.favourites_list import FavouritesList, Favourites_list_schema, Favourites_lists_schema


favourites_list_bp = Blueprint('favourites_list', __name__, url_prefix='/favourites_list')

@favourites_list_bp.route('/<int:favourites_list_id>')
def get_favourites_list(favourites_list_id):
    stmt = db.select(FavouritesList).filter_by(id=favourites_list_id)
    favourites_list = db.session.scalar(stmt)
    return Favourites_list_schema.dump(favourites_list)



@favourites_list_bp.route('/')
def get_all_favourites_list():
    stmt = db.select(FavouritesList).order_by(FavouritesList.date_added.desc())
    favourites_list = db.session.scalars(stmt)
    return Favourites_lists_schema.dump(favourites_list)

