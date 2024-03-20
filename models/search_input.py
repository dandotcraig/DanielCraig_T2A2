from init import db, ma
from marshmallow import fields
from datetime import datetime

class SearchInput(db.Model):
    __tablename__ = "search_input"

    id = db.Column(db.Integer, primary_key=True)
    search_input = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow) 

    favourite_search = db.relationship("FavouriteSearch", back_populates="search_input")

class SearchInputSchema(ma.Schema):

    favourites_list = fields.List(fields.Nested('FavouritesListSchem', only=['id']))

    favourite_search = fields.List(fields.Nested('FavouriteSearchSchema'))

    class Meta:
        fields = ('id', 'search_input',  'date_added', 'favourites_list')
        ordered = True

Search_input_Schema = SearchInputSchema()
Search_inputs_Schema = SearchInputSchema(many=True)


# HOW I WANT IT RETURNED

# {
#   "id": 1,
#   "date": "2024-03-15",
#   "search_input": "restaurants",
#   "favourites_list": [
#     {
#       "date": "2024-03-15",
#       "account": {
#         "id": 1,
#         "account_type": "personal"
#       }
#     }
#   ]
# }
