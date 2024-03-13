from init import db, ma
from marshmallow import fields
# from models.favourite_search import association_table

# formating the user table
class SearchInput(db.Model):
    __tablename__ = "search_input"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    search_input = db.Column(db.String, nullable=False)

    favourites_list = db.relationship('FavouriteSearch', secondary='favourite_search', back_populates='search_input', cascade='all, delete')

# structure of the database
class SearchInputSchema(ma.Schema):

    favourites_list = fields.List(fields.Nested('FavouritesListSchem', exclude=['user']))

    class Meta:
        fields = ('id', 'search_input', 'date')

Search_input_Schema = SearchInputSchema()
Search_inputs_Schema = SearchInputSchema(many=True)


    # HOW I WANT IT RETURNED
    # {
    #   id: 1,
    #   data: [00/00/00],
    #   search_input: Favourited_search_result
    #   favourites_list: [
    #       {id: 1 account: 1}
    #       {id: 2 account: 2}
    #       etc
    # }