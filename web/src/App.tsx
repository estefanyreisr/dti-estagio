import { useEffect, useState } from 'react'
import axios from 'axios'
import Table from 'react-bootstrap/Table'

import './App.css'

function App() {
  const [books, setBooks] = useState([])

  useEffect(() => {
    axios.get("http://localhost:3000/livros")
      .then(response => {
        const axiosData = response.data
        setBooks(axiosData.data)
      })

  }, [])

  return (
    <>

      <div>
        <h1>Livros</h1>

        <Table striped bordered hover>
          <thead>
            <tr>
              <th>ID</th>
              <th>Título</th>
              <th>Autor</th>
              <th>Gênero</th>
              <th>Editora</th>
              <th>Número de Páginas</th>
              <th>Data de Lançamento</th>
            </tr>
          </thead>
          <tbody>
            {books.map((book) => {
              return (
                <tr key={book.id}>
                  <td>{book.id}</td>
                  <td>{book.titulo}</td>
                  <td>{book.autor}</td>
                  <td>{book.genero}</td>
                  <td>{book.editora}</td>
                  <td>{book.numero_paginas}</td>
                  <td>{book.data_lancamento}</td>
                </tr>
              )
            })}
          </tbody>
        </Table>

      </div>

    </>

  )
}

export default App
