from flask import Blueprint, jsonify


book_route_bp = Blueprint("book_route", __name__)

@book_route_bp.route("/livros", methods = ["POST"] )
def create_new_book():
    return jsonify({"estou" : "aqui"}), 201