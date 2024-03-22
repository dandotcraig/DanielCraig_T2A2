from init import db, ma
from marshmallow import fields
from datetime import datetime

class FavouriteSearch(db.Model):
    __tablename__ = "favourite_search"

    id = db.Column(db.Integer, primary_key=True)
    search_input_id = db.Column(db.Integer, db.ForeignKey("search_input.id"))
    favourites_list_id = db.Column(db.Integer, db.ForeignKey("favourites_list.id")) 
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    search_input = db.relationship("SearchInput", back_populates="favourite_search")   

    favourites_list = db.relationship("FavouritesList", back_populates="favourite_search")   

    

class FavouriteSearchSchema(ma.Schema):
    main_favourite_search_id = fields.Integer(attribute='id')

    search_input = fields.Nested('SearchInputSchema', only=('search_input', 'date_added'))

    class Meta:
        fields = ('main_favourite_search_id', 'search_input', 'favourites_list_id', 'date_added')


Favourite_search_schema = FavouriteSearchSchema()
Favourite_searchs_schema = FavouriteSearchSchema(many=True)
