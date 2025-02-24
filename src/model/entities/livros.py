from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer, Date

class Livros(Base):
    __tablename__= "Livros"
    id = Column(Integer, primary_key= True, autoincrement=True)
    titulo = Column(String, nullable=False) 
    autor =  Column(String, nullable=False)
    genero = Column(String, nullable=True) 
    editora = Column(String, nullable=True)
    numero_paginas = Column(Integer, nullable=True)
    data_lancamento = Column(Date, nullable=False)