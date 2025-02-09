# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash



class Movies(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text())
    poster = db.Column(db.String(200))
    created_at= db.Column(db.DateTime())


    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
