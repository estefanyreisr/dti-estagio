from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

from src.model.repositories.livros_repository import LivrosRepository
from src.controllers.books.books_manager import BooksManager

from src.validators.books_validator import book_creator_validator


book_route_bp = Blueprint("book_route", __name__)

@book_route_bp.route("/livros", methods = ["POST"] )
def create_new_book():
    
    book_creator_validator(request)
    
    http_request = HttpRequest(body=request.json)
    
    book_repo = LivrosRepository()
    
    books_creator = BooksManager(book_repo)
    
    http_response = books_creator.create(http_request)
    
    print('http_response', http_response.body)
    
    return jsonify(http_response.body), http_response.status_code

@book_route_bp.route("/livros", methods = ["GET"] )
def read_books():
       
    book_repo = LivrosRepository()
    
    books_controller = BooksManager(book_repo)
    
    http_response = books_controller.read_all()
    
    return jsonify(http_response.body), http_response.status_code

@book_route_bp.route("/livros/<book_id>", methods = ["DELETE"] )
def delete_book_by_id(book_id):
    
    http_request = HttpRequest(param={"book_id": book_id})
    
    book_repo = LivrosRepository()
    
    books_controller = BooksManager(book_repo)
    
    http_response = books_controller.delete(http_request)
    
    print('http_response', http_response.body)
    
    return jsonify(http_response.body), http_response.status_code
