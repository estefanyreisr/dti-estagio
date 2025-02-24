from src.model.configs.connection import DBConnectionHandler
from src.model.entities.livros import Livros
from datetime import date
from src.model.repositories.interfaces.livros_repository import LivrosRepositoryInterface

class LivrosRepository(LivrosRepositoryInterface) :
    def insert(self, book_title:str, book_author:str, book_gender:str, book_publisher:str, book_pages_number:int, book_date_release:date) -> None:
       with DBConnectionHandler() as db:
           try:
                new_book = Livros(
                   titulo = book_title,
                   autor = book_author,
                   genero = book_gender,
                   editora = book_publisher,
                   numero_paginas = book_pages_number,
                   data_lancamento = book_date_release 
               ) 
                db.session.add(new_book)
                db.session.commit()
           except Exception as exception:
               db.session.rollback()
               raise exception
    
    
    
    def select_book_by_title(self, book_title: str) -> Livros:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Livros)
                .filter(Livros.titulo == book_title)
                .one_or_none()
            )
            return data
    
    def get_all_books(self) -> list:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Livros)
                .all()
            )
            return data
    
    def update_book(self, book_id: int, new_title: str) -> None:
        with DBConnectionHandler() as db:
            try:
                book = db.session.query(Livros).filter(Livros.id == book_id).one_or_none()
                if book:
                    book.titulo = new_title
                    db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def delete_book(self, book_title: str) -> None:
            with DBConnectionHandler() as db:
                try:
                    # Encontrar o livro pelo título
                    book = db.session.query(Livros).filter(Livros.titulo == title).one_or_none()
                    
                    if book:
                        # Se o livro existir, deleta o livro
                        db.session.delete(book)
                        db.session.commit()
                    else:
                        raise ValueError(f"Livro com o título '{title}' não encontrado.")
                except Exception as exception:
                    db.session.rollback()
                    raise exception

            
            
            
           
           
           
           
           
           
           
           
