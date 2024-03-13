from init import db, ma
from marshmallow import fields
# from models.favourite_search import FavouriteSearch

class FavouritesList(db.Model):
    __tablename__ = "favourites_list"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    

    account_list = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    account = db.relationship('Account', back_populates='favourites_list')

    search_input = db.relationship('FavouriteSearch', secondary='favourite_search', back_populates='favourites_list')

# structure of the database
class FavouritesListSchema(ma.Schema):

    account = fields.Nested('AccountSchema', only = ['name', 'email'])
    # HERE IS WHERE I WILL DISPLAY THE SEARCH RESULTS
    search_input = fields.Nested('SearchInputSchema', only = ['search_input'])
    
    class Meta:
        fields = ('id', 'date', 'user_id', 'account', 'search_input')

Favourites_list_schema = FavouritesListSchema()
Favourites_lists_schema = FavouritesListSchema(many=True)

    # HOW I WANT IT RETURNED
    # {
    #   id: 1,
    #   data: [00/00/00],
    #   account_id: 000001,
    #   search_input: [
    #       {id: 1 search_input: Favourited_search_result}
    #       {id: 2 search_input: Favourited_search_result}
    #       etc
    #   ]
    # }
