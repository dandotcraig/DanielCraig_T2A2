from init import db

class FavouriteSearch(db.Model):
    __tablename__ = "favourite_search"

    id = db.Column(db.Integer, primary_key=True)
    search_input_id = db.Column(db.Integer, db.ForeignKey("search_input.id"))
    favourites_list_id = db.Column(db.Integer, db.ForeignKey("favourites_list.id")) 