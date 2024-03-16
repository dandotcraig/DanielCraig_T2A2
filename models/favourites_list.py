from init import db, ma
from marshmallow import fields
from models.favourite_search import FavouriteSearch
from datetime import datetime

class FavouritesList(db.Model):
    __tablename__ = "favourites_list"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    account = db.relationship('Account', back_populates='favourites_list', cascade='all, delete')

    favourite_search = db.relationship("FavouriteSearch", back_populates="favourites_list")


class FavouritesListSchema(ma.Schema):

    account = fields.Nested('AccountSchema', only=('id',))

    search_input = fields.Nested('SearchInputSchema', only = ['search_input'])
    
    class Meta:
        fields = ('id', 'date', 'account', 'date_added', 'search_input')
        ordered=True

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
