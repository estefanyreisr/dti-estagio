from flask import Flask
from flask_cors import CORS
from src.main.routes.book import book_route_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(book_route_bp)