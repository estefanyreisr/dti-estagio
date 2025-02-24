from flask import Flask
from src.main.routes.book import book_route_bp

app = Flask(__name__)

app.register_blueprint(book_route_bp)