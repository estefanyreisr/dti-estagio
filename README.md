# Teste de estágio Full Stack Dti Digital

## Execução do Backend

O BackEnd foi feito com Python 3 utilizando o micro-framework web [Flask](https://flask.palletsprojects.com/en/stable/installation/){:target="_blank"}. Para o mapeamento com o banco de dados, foi usada a biblioteca [SQLAlchemy](https://www.sqlalchemy.org/download.html#current){:target="_blank"}.

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
Foi utilizado o [DBeaver](https://dbeaver.io/){:target="_blank"} para a visualização dos dados do banco de dados.

O [Postman](https://www.postman.com/){:target="_blank"} foi usado para testar as requisições.

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

O FrontEnd foi feito com [ReactJS](https://react.dev/){:target="_blank"} e TypeScript. 

Para a integração com o BackEnd foi utilizada a biblioteca [axios](https://axios-http.com/docs/intro){:target="_blank"} e para visualização foi usado o [React Bootstrap](https://react-bootstrap.netlify.app/){:target="_blank"}.

### Comandos

```
$ cd web 
$ npm install # para baixar os pacotes
$ npm run dev # para rodar a aplicação
```