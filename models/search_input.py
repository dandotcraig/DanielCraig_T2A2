from init import db, ma
from marshmallow import fields
# from models.favourite_search import association_table

# formating the user table
class SearchInput(db.Model):
    __tablename__ = "search_input"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    search_input = db.Column(db.String, nullable=False)

    favourites_list = db.relationship('FavouritesList', secondary='favourite_search', back_populates='search_input')

# structure of the database
class SearchInputSchema(ma.Schema):

    favourites_list = fields.List(fields.Nested('FavouritesListSchem', exclude=['user']))

    class Meta:
        fields = ('id', 'date', 'search_input', 'favourites_list')

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
