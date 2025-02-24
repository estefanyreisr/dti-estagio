from src.model.repositories.livros_repository import LivrosRepository

from src.model.entities.livros import Livros

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

from datetime import datetime

class BooksManager:
    def __init__(self, book_repo: LivrosRepository):
        self.__book_repo = book_repo
        
    def create(self, http_request: HttpRequest) -> HttpResponse:
        book_data = http_request.body["data"]
        
        book_name = book_data["titulo"] 
        
        self.__check_book_title(book_name)
        self.__insert_book(book_data)
        
        return self.__format_response_create(book_data)
        
    
    def __check_book_title(self, book_title: str) -> None:
        response = self.__book_repo.select_book_by_title(book_title)
        
        if response:
            raise Exception("Book already exists")
        
    
    def __insert_book(self, book_data: dict) -> None:
        
        book_title = book_data["titulo"]
        book_author = book_data["autor"]
        book_publisher = book_data["editora"]
        book_gender = book_data["genero"]
        book_pages = book_data["numero_paginas"]
        
        book_date_release = datetime.strptime(book_data["data_lancamento"], '%Y-%m-%d').date()
        
        
        self.__book_repo.insert(
            book_title=book_title,
            book_author=book_author,
            book_publisher=book_publisher,
            book_gender=book_gender,
            book_pages_number=book_pages,
            book_date_release=book_date_release
        )
        
    def __format_response_create(self, book_data: dict) -> HttpResponse:
        return HttpResponse(
            status_code=201,
            body={
                "message": "Livro criado com sucesso",
                "data": book_data
            }
        )
        
    def read_all(self) -> HttpResponse:
        books = self.__book_repo.get_all_books()
        
        return self.__format_response_read_all(books)
    

    def __format_response_read_all(self, books: list[Livros]) -> HttpResponse:
        books_data = []
        for b in books:
            books_data.append({
                "titulo": b.titulo,
                "autor": b.autor,
                "editora": b.editora,
                "genero": b.genero,
                "numero_paginas": b.numero_paginas,
                "data_lancamento": b.data_lancamento.strftime('%Y-%m-%d')
            })
        return HttpResponse(
            status_code=200,
            body={
                "data": books_data
            }
        )
        
    
    def delete(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.param["book_id"]
        
        self.__book_repo.delete_book(int(id))
        
        return self.__format_response_delete(id)
    
    def __format_response_delete(self, book_id: str) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "message": "Livro com o id " + book_id + " foi deletado com sucesso"
            }
        )
        
    
    def read(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.param["book_id"]
        
        book = self.__book_repo.get_book_by_id(int(id))
        
        return self.__format_response_read(book)
    
    def __format_response_read(self, book: Livros) -> HttpResponse:
        book_formatted = {
            "titulo": book.titulo,
            "autor": book.autor,
            "editora": book.editora,
            "genero": book.genero,
            "numero_paginas": book.numero_paginas,
            "data_lancamento": book.data_lancamento.strftime('%Y-%m-%d')
        }
        
        return HttpResponse(
            status_code=200,
            body={
                "data": book_formatted
            }
        )
        
    def update(self, http_request: HttpRequest) -> HttpResponse:
        book_data = http_request.body["data"]
        book_id = http_request.param["book_id"]
        
        self.__book_repo.update_book(book_id=book_id, book_info=book_data)
        
        return self.__format_response_update(book_data)
        
    def __format_response_update(self, book_data: dict) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "message": "Livro atualizado com sucesso",
                "data": book_data
            }
        )
