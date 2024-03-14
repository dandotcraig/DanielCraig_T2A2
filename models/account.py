from init import db, ma
import enum
from sqlalchemy import Enum
from marshmallow import fields

class BusinessPersonal(enum.Enum):
    business = 'business'
    personal = 'personal'

class Account(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(Enum(BusinessPersonal), nullable=False)
   
    users = db.relationship('User', back_populates='account')

    favourites_list = db.relationship('FavouritesList', back_populates='account', cascade='all, delete')

class AccountSchema(ma.Schema):

    users = fields.Nested('UserSchema', only = ['name', 'email'])

    favourites_list = fields.Nested('FavouritesListSchema')
    
    class Meta:
        fields = ('id', 'account_type', 'users', 'favourites_list')

Account_schema = AccountSchema()
Accounts_schema = AccountSchema(many=True)

# HOW I WANT IT RETURNED
# {
#   "id": 1,
#   "account_type": "personal",
#   "users": [
#     {
#       "name": "John Doe",
#       "email": "john@example.com"
#     }
#   ],
#   "favourites_list": [
#     {
#       "id": 1,
#       "date": "2024-03-15",
#       "search_input": [
#         {
#           "search_input": "restaurants",
#           "date": "2024-03-15"
#         }
#       ]
#     }
#   ]
# }