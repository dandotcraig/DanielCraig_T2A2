from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    # account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    
    account = db.relationship('Account', back_populates='user', cascade='all, delete')
    

class UserSchema(ma.Schema):

    account = fields.List(fields.Nested('AccountSchema', exclude=['user']))
    
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'account')

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])

# HOW I WANT IT RETURNED

# User:
# {
#   "id": 1,
#   "name": "John Doe",
#   "email": "john@example.com",
#   "is_admin": false,
#   "account": {
#     "id": 1,
#     "account_type": "personal"
#   }
# }

