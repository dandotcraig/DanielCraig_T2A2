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

    user_id = db.Column(db.Integer, db.foreignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='account')

class AccountSchema(ma.Schema):
    account = fields.nested('UserSchema', only = ['name', 'email'])
    class Meta:
        fields = ('id', 'account_type', 'user')

Account_schema = AccountSchema()
Accounts_schema = AccountSchema(many=True)