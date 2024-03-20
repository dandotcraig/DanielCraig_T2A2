from init import db, ma
from marshmallow import fields
from datetime import datetime

class Account(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    is_business_account = db.Column(db.Boolean, default=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow) 
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
   
    user = db.relationship('User', back_populates='account')

    favourites_list = db.relationship('FavouritesList', back_populates='account', cascade='all, delete')

class AccountSchema(ma.Schema):

    user = fields.Nested('UserSchema', only = ['name', 'email'])

    favourites_list = fields.Nested('FavouritesListSchema', only = ['id', 'favourite_search'])
    
    class Meta:
        fields = ('id', 'is_business_account', 'user', 'date_added')
        ordered=True

Account_schema = AccountSchema()
Accounts_schema = AccountSchema(many=True)

