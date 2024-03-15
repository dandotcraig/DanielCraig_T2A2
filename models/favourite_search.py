from init import db

class FavouriteSearch(db.Model):
    __tablename__ = "favourite_search"

    id = db.Column(db.Integer, primary_key=True)
    search_input_id = db.Column(db.Integer, db.ForeignKey("search_input.id"))
    favourites_list_id = db.Column(db.Integer, db.ForeignKey("favourites_list.id")) 

    favourites_list = db.relationship("FavouritesList", back_populates="favourite_search")   

    search_input = db.relationship("SearchInput", back_populates="favourite_search")   

# HOW I WANT IT RETURNED

# {
#   "id": 1,
#   "search_input_id": 1,
#   "favourites_list_id": 1
# }