CREATE TABLE Livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    genero TEXT,
    editora TEXT,
    lancamento DATE
);
