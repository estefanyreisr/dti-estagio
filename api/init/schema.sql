CREATE TABLE Livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    genero TEXT,
    editora TEXT,
    numero_paginas INTEGER,
    data_lancamento DATE NOT NULL
);
