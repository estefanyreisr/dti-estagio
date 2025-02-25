from abc import ABC, abstractmethod
from typing import List, Optional
from src.model.entities.livros import Livros
from datetime import date


class LivrosRepositoryInterface(ABC):
        
    @abstractmethod
    def insert(self, book_title:str, book_author:str, book_gender:str, book_publisher:str, book_pages_number:int, book_date_release:date) -> None:
        """Insere um novo livro no banco de dados"""
        pass
    
    @abstractmethod
    def select_book_by_title(self, titulo: str) -> Optional[Livros]:
        """Busca um livro pelo título e retorna um objeto Livros ou None se não encontrado"""
        pass

    @abstractmethod
    def get_all_books(self) -> List[Livros]:
        """Retorna todos os livros cadastrados no banco"""
        pass
    
    @abstractmethod
    def update_book(self, book_id: int, new_title: str) -> None:
        """Atualiza o título de um livro pelo ID"""
        pass
    
    @abstractmethod
    def delete_book(self, book_id: int) -> None:
        """Deleta um livro pelo ID"""
        pass
    
    @abstractmethod
    def get_book_by_id(self, book_id: int) -> None:
        """Busca um livro pelo ID e retorna um objeto Livros ou None se não encontrado"""
        pass