from flask import Blueprint

from init import db
from models.search_input import SearchInput, Search_input_Schema, Search_inputs_Schema


search_input_bp = Blueprint('search_input', __name__, url_prefix='/search_input')

# HIDDEN http://127.0.0.1:8080/search_input/1
@search_input_bp.route('/<int:search_input>')
def get_search_input(search_input):
    stmt = db.select(SearchInput).filter_by(id=search_input)
    search_input = db.session.scalar(stmt)
    return Search_input_Schema.dump(search_input)


# http://127.0.0.1:8080/search_input
@search_input_bp.route('/')
def get_all_search_input():
    stmt = db.select(SearchInput).order_by(SearchInput.date_added.desc())
    search_input = db.session.scalars(stmt)
    return Search_inputs_Schema.dump(search_input)



