from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    account = db.relationship('Account', back_populates='user', uselist=False)
    
class UserSchema(ma.Schema):

    main_users_id = fields.Integer(attribute='id')

    account = fields.Nested('AccountSchema', exclude=['user'])
    
    class Meta:
        fields = ('main_users_id', 'name', 'email', 'password', 'is_admin', 'account')

User_schema = UserSchema(exclude=['password'])
Users_schema = UserSchema(many=True, exclude=['password'])


