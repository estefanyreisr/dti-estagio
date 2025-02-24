from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

from src.validators.books_validator import book_creator_validator


book_route_bp = Blueprint("book_route", __name__)

@book_route_bp.route("/livros", methods = ["POST"] )
def create_new_book():
    
    book_creator_validator(request)
    
    http_request = HttpRequest(body=request.json)
    
    http_response = HttpResponse(body=http_request.body, status_code=201)
    
    return jsonify(http_response.body), http_response.status_code