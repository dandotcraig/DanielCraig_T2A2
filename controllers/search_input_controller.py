from flask import Blueprint, request
from init import db
from models.search_input import SearchInput, Search_input_Schema, Search_inputs_Schema
from flask_jwt_extended import jwt_required, get_jwt_identity

search_input_bp = Blueprint('search_input', __name__, url_prefix='/search_input')

# Get all search inputs (auth)
# http://127.0.0.1:8080/search_input
@search_input_bp.route('/')
@jwt_required()
def get_all_search_input():
    stmt = db.select(SearchInput).order_by(SearchInput.date_added.desc())
    search_input = db.session.scalars(stmt)
    return Search_inputs_Schema.dump(search_input)


# Get INDIVIDUAL search input (auth)
# Admin http://127.0.0.1:8080/search_input/1
@search_input_bp.route('/<int:search_input>')
@jwt_required()
def get_search_input(search_input):
    stmt = db.select(SearchInput).filter_by(id=search_input)
    search_input = db.session.scalar(stmt)
    return Search_input_Schema.dump(search_input)

# Create search_input
# Create http://127.0.0.1:8080/search_input
@search_input_bp.route('/', methods = ['POST'])
def input_search_input():
    body_data = Search_input_Schema.load(request.get_json())
    # Create a new card model instance
    input_search_input = SearchInput(
        search_input = body_data.get('search_input')
    )
    # Add that to the session and commit
    db.session.add(input_search_input)
    db.session.commit()
    # return the newly created card
    return Search_input_Schema.dump(input_search_input), 201