from init import db, ma
from marshmallow import fields
from models.favourite_search import FavouriteSearch
from datetime import datetime


class FavouritesList(db.Model):
    __tablename__ = "favourites_list"

    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), unique=True, nullable=True)
    account = db.relationship('Account', back_populates='favourites_list')

    favourite_search = db.relationship("FavouriteSearch", back_populates="favourites_list")


class FavouritesListSchema(ma.Schema):

    main_favourites_list_id = fields.Integer(attribute='id')

    account = fields.Nested('AccountSchema', only=('main_account_id', 'user'))

    favourite_search = fields.List(fields.Nested('FavouriteSearchSchema', only=('search_input', 'date_added')))

    class Meta:
        fields = ('main_favourites_list_id', 'account', 'date_added', 'favourite_search')
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
