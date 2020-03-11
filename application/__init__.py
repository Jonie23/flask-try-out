from flask import Flask
from instance.config import Config
 

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

# blueprints
from application.users.routes import users_blueprint
from application.recipes.routes import recipes_blueprint

#register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)