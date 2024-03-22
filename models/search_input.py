from init import db, ma
from marshmallow import fields
from datetime import datetime
from marshmallow.validate import Length

class SearchInput(db.Model):
    __tablename__ = "search_input"

    id = db.Column(db.Integer, primary_key=True)
    search_input = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow) 

    favourite_search = db.relationship("FavouriteSearch", back_populates="search_input")

class SearchInputSchema(ma.Schema):

    main_search_input_id = fields.Integer(attribute='id')

    search_input = fields.String(validate=Length(min=3, error="Search must be atleast 2 characters in length"))

    favourites_list = fields.List(fields.Nested('FavouritesListSchema', only=['main_favourites_list_id']))

    # favourite_search = fields.List(fields.Nested('FavouriteSearchSchema'))

    class Meta:
        fields = ('main_search_input_id ', 'search_input', 'date_added', 'favourites_list')
        ordered = True

Search_input_Schema = SearchInputSchema()
Search_inputs_Schema = SearchInputSchema(many=True)


