from .livros_repository import LivrosRepository
from datetime import datetime

#@pytest.mark.skip("Insert in db") 
"""def test_insert_book():
    book_title = "Doctor House"
    book_author = "Ana C."
    book_gender = "Médico"
    book_publisher = "HBO"
    book_pages_number = 641
    book_date_release = datetime.strptime("2025-02-03", '%Y-%m-%d').date()
        
    book_repo = LivrosRepository()
    book_repo.insert(book_title, book_author, book_gender, book_publisher, book_pages_number, book_date_release ) """
    

    
def test_select_book_by_title():
    book_title = "Harry Poter e a Pedra Filosofal"
    book_repo = LivrosRepository()
    
    book = book_repo.select_book_by_title(book_title)
    
    print(book)
    print(book.titulo)
    print(book.id)
    
    
def test_get_all_books():
    book_repo = LivrosRepository()
    
    books = book_repo.get_all_books()
    
    assert books is not None
    assert isinstance(books, list)  # Garante que retorna uma lista
    assert len(books) > 0  # Garante que há pelo menos um livro cadastrado
    
    for book in books:
        assert hasattr(book, "id")  # Garante que cada livro tem um ID
        assert hasattr(book, "titulo")  # Garante que cada livro tem um título
        print(f"ID: {book.id}, Título: {book.titulo}")
    

"""def test_update_book():
    book_repo = LivrosRepository()

    # Supondo que já exista um livro no banco
    old_title ="Edição Especial"
    new_title = "Jogos Vorazes" 

    # Buscar o livro original pelo título antigo
    book = book_repo.select_book_by_title(old_title)
    assert book is not None, "O livro não foi encontrado no banco de dados."

    # Atualizar o título do livro
    book_repo.update_book(book.id, new_title)

    # Buscar o livro novamente pelo novo título
    updated_book = book_repo.select_book_by_title(new_title)
    assert updated_book is not None, "O livro atualizado não foi encontrado."
    assert updated_book.titulo == new_title

    print(f"Livro atualizado com sucesso: ID {updated_book.id}, Novo Título: {updated_book.titulo}")"""
    
    
def test_delete_book_by_title():
    book_repo = LivrosRepository()

    # Criar um livro para deletar no teste
    book_title = "Livro Temporário"
    book_repo.insert(book_title, "Autor Teste", "Ficção", "Editora X", 300, datetime.strptime("2023-01-01", '%Y-%m-%d').date())

    # Verificar se o livro foi inserido corretamente
    book = book_repo.select_book_by_title(book_title)
    assert book is not None, f"O livro '{book_title}' não foi inserido corretamente."

    # Deletar o livro pelo título
    book_repo.delete_book(book_title)

    # Verificar se o livro foi realmente deletado
    deleted_book = book_repo.select_book_by_title(book_title)
    assert deleted_book is None, f"O livro '{book_title}' ainda está no banco de dados após a exclusão."

    print(f"Livro '{book_title}' deletado com sucesso!")