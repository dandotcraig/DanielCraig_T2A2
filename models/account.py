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
   
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    # user = db.relationship('User', back_populates='account')

    # favourites_list_id = db.Column(db.Integer, db.ForeignKey('favourites_list.id'), nullable=False)
    favourites_list = db.relationship('FavouritesList', back_populates='account')

class AccountSchema(ma.Schema):

    user = fields.Nested('UserSchema', only = ['name', 'email'])

    favourites_list = fields.Nested('FavouritesListSchema', only = ['search_input'])
    
    class Meta:
        fields = ('id', 'account_type', 'user', 'favourites_list')

Account_schema = AccountSchema()
Accounts_schema = AccountSchema(many=True)

    # HOW I WANT IT RETURNED
    # {
    #   id: 1,
    #   account: [ACCOUNT TYPE]
    #   users: [
    #       {id: 1 name: xxx email: xxx}
    #       {id: 2 name: xxx email: xxx}
    #       etc
    #   ]
    # }