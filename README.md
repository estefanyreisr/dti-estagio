# Teste de estágio Full Stack Dti Digital

## Execução do Backend

O BackEnd foi feito com Python 3 utilizando o micro-framework web [Flask](https://flask.palletsprojects.com/en/stable/installation/). Para o mapeamento com o banco de dados, foi usada a biblioteca [SQLAlchemy](https://www.sqlalchemy.org/download.html#current).

A aplicação roda na porta `3000`.

- Validação de Entrada: foi utilizada a biblioteca [Cerberus](https://docs.python-cerberus.org/n) para a validação de entrada dos dados.
- Testes: foi utilizada a biblioteca [Pytest](https://docs.pytest.org/en/stable/) para testes.

### Criação do ambiente virtual

```
$ python3 -m venv apivenv # cria um ambiente virtual chamado apivenv
$ . .\apivenv\Scripts\activate` # ativa o ambiente virtual (se for Windows)
```

### Conexão com o banco de dados

1. Criação do arquivo `schema.db` em `/api`.
2. Na pasta `/api`, foi rodado o script:
```
$ python3 
>>> import sqlite3
>>> sqlite3.connect('schema.db')
>>> exit()
```
3. O script utilizado para criar as tabelas no banco de dados SQLite está em `/api/init/schema.sql`

Foi utilizado o [DBeaver](https://dbeaver.io/) para a visualização dos dados do banco de dados.

O [Postman](https://www.postman.com/) foi usado para testar as requisições.

### Para rodar a api 
```
$ pip3 install -r .\requirements.txt # para baixar os pacotes
$ python run.py 
```

### Para rodar o arquivo de testes 
```
$ pytest -s -v .\src\model\repositories\livros_repository_test.py
```

## Execução do Frontend

O FrontEnd foi feito com [ReactJS](https://react.dev/) e TypeScript. 

Para a integração com o BackEnd foi utilizada a biblioteca [axios](https://axios-http.com/docs/intro) e para visualização foi usado o [React Bootstrap](https://react-bootstrap.netlify.app/).

### Comandos

```
$ cd web 
$ npm install # para baixar os pacotes
$ npm run dev # para rodar a aplicação
```

## Descrição do Recurso

Foi utilizado o recurso `Livro` com as seguintes:
- id: campo numérico, chave primário e autoincremental;
- titulo: campo texto (string) e obrigatório;
- autor: campo texto (string) e obrigatório;
- genero: campo texto (string) e opcional;
- editora: campo texto (string) e opcional;
- numero_paginas: campo numérico e opcional;
- data_lancamento: campo de data e obrigatório;

## Descrição das rotas
### 1. Cadastrar Recurso
Endpoint: POST `http://localhost:3000/livros`

Objetivo: Cadastrar um novo livro.

Exemplo de body:
```
{
    "data": {
        "titulo": "Divergente",
        "autor": "Ana Maria Braga",
        "genero": "Aventura",
        "editora": "Geek",
        "numero_paginas":1200,
        "data_lancamento": "2025-12-17"
    }
}   
```
Exemplo de resposta:
```
{
    "data": {
        "autor": "Ana Maria Braga",
        "data_lancamento": "2025-12-17",
        "editora": "Geek",
        "genero": "Aventura",
        "numero_paginas": 1200,
        "titulo": "Wicked"
    },
    "message": "Livro criado com sucesso"
}
```

### 2. Buscar por ID
Endpoint: GET `http://localhost:3000/livros/1`

Objetivo: Buscar pelo ID de um livro e retornar seus detalhes.

Exemplo de resposta:
```
{
    "data": {
        "autor": "J.K Rolling",
        "data_lancamento": "2020-12-04",
        "editora": "A Ordem",
        "genero": "fantasy",
        "numero_paginas": 1548,
        "titulo": "O Senhor dos Anéis"
    }
}
```

### 3. Listar Recursos
Endpoint: GET `http://localhost:3000/livros`

Objetivo: Exibe todos os livros no banco de dados, exibindo informações relevantes.

Exemplo de resposta:
```
{
    "data": [
        {
            "autor": "J.K Rolling",
            "data_lancamento": "2020-12-04",
            "editora": "A Ordem",
            "genero": "fantasy",
            "id": 1,
            "numero_paginas": 1548,
            "titulo": "O Senhor dos Anéis"
        },
        {
            "autor": "J.K.R",
            "data_lancamento": "2015-12-01",
            "editora": "A Ordem",
            "genero": "Fantasia",
            "id": 3,
            "numero_paginas": 2365,
            "titulo": "Harry Poter e a Pedra Filosofal"
        },
        {
            "autor": "Maria Braga",
            "data_lancamento": "2017-10-16",
            "editora": "TNYT",
            "genero": "Ficçao",
            "id": 4,
            "numero_paginas": 789,
            "titulo": "Jogos Vorazes"
        }
    ]
}
```

### 4. Atualizar Recurso
Endpoint: PUT `http://localhost:3000/livros/3`

Objetivo: Exibe todos os livros no banco de dados, exibindo informações relevantes.
Exemplo de body:
```
{
    "data": {
        "titulo": "House of the drag",
        "autor": "Ana Maria Braga",
        "genero": "Aventura",
        "editora": "Geek",
        "numero_paginas":1200,
        "data_lancamento": "2025-12-17"
    }
}     
```

Exemplo de resposta:
```
{
    "data": {
        "titulo": "House of the drag",
        "autor": "Ana Maria Braga",
        "genero": "Aventura",
        "editora": "Geek",
        "numero_paginas":1200,
        "data_lancamento": "2025-12-17"
    }
    "message": "Livro atualizado com sucesso"
}

```

### 5. Deletar Recurso
Endpoint: DELETE `http://localhost:3000/livros/3`

Objetivo: Remover um livro existente do banco de dados com base no seu ID.

Exemplo de resposta:
```
{
    "message": "Livro com o id 3 foi deletado com sucesso"
}
```
