from init import db, ma
from marshmallow import fields
from models.favourite_search import FavouriteSearch

class FavouritesList(db.Model):
    __tablename__ = "favourites_list"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    
    account = db.relationship('Account', back_populates='favourites_list', cascade='all, delete')

    search_input = db.relationship('SearchInput', secondary='favourite_search', back_populates='favourites_list')

class FavouritesListSchema(ma.Schema):

    account = fields.Nested('AccountSchema', only=('id',))

    search_input = fields.Nested('SearchInputSchema', only = ['search_input'])
    
    class Meta:
        fields = ('id', 'date', 'account', 'search_input')

Favourites_list_schema = FavouritesListSchema()
Favourites_lists_schema = FavouritesListSchema(many=True)

# HOW I WANT IT RETURNED

# {
#   "id": 1,
#   "date": "2024-03-15",
#   "account": {
#     "id": 1
#   },
#   "search_input": [
#     {
#       "search_input": "restaurants",
#       "date": "2024-03-15"
#     }
#   ]
# }
