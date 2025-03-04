from flask import Flask
from config import Config

from .routes import global_scope

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

#BLUEPRINTS REGISTERS
app.register_blueprint(global_scope, url_prefix='/')