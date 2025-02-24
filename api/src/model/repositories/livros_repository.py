from src.model.configs.connection import DBConnectionHandler
from src.model.entities.livros import Livros
from datetime import date, datetime
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
    
    def get_all_books(self) -> list[Livros]:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Livros)
                .all()
            )
            return data
    
    def update_book(self, book_id: int, book_info: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                book = db.session.query(Livros).filter(Livros.id == book_id).one_or_none()
                if book:
                    book.titulo = book_info["titulo"]
                    book.autor = book_info["autor"]
                    book.genero = book_info["genero"]
                    book.editora = book_info["editora"]
                    book.numero_paginas = book_info["numero_paginas"]
                    book.data_lancamento = datetime.strptime(book_info["data_lancamento"], '%Y-%m-%d').date()
                    db.session.commit()
                    
                else:
                    raise ValueError(f"Livro com o id '{book_id}' não encontrado.")
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def delete_book(self, book_id: int) -> None:
            with DBConnectionHandler() as db:
                try:
                    # Encontrar o livro pelo id
                    book = db.session.query(Livros).filter(Livros.id == book_id).one_or_none()
                    if book:
                        # Se o livro existir, deleta o livro
                        db.session.delete(book)
                        db.session.commit()
                    else:
                        raise ValueError(f"Livro com o id '{book_id}' não encontrado.")
                except Exception as exception:
                    db.session.rollback()
                    raise exception
                
    def get_book_by_id(self, book_id: int) -> None:
        with DBConnectionHandler() as db:
            # Encontrar o livro pelo id
            book = db.session.query(Livros).filter(Livros.id == book_id).one_or_none()
            
            if book:
                return book
            else:
                raise ValueError(f"Livro com o id '{book_id}' não encontrado.")
                

     

       
            
            
           
           
           
           
           
           
           
           
