import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User, Character, Planet, FavoriteCharacter, FavoritePlanet

def setup_admin(app):
    app.secret_key = os.getenv("FLASK_APP_KEY", "default_key")
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
    admin = Admin(app, name="Admin", template_mode="bootstrap3")

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(FavoriteCharacter, db.session))
    admin.add_view(ModelView(FavoritePlanet, db.session))

