from .livros_repository import LivrosRepository
from datetime import datetime

#@pytest.mark.skip("Insert in db")

def test_insert_book():
    book_title = "Squid Game"
    book_author = "João"
    book_gender = "Suspense"
    book_publisher = "Vogue"
    book_pages_number = 698
    book_date_release = datetime.strptime("2011-11-11", '%Y-%m-%d').date()
        
    book_repo = LivrosRepository()
    book_repo.insert(book_title, book_author, book_gender, book_publisher, book_pages_number, book_date_release )
    

    
    
    