CREATE DATABASE Leitura_Conversas;
drop DATABASE Leitura_Conversas;

USE Leitura_Conversas;

CREATE TABLE Livros (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    genero TEXT NOT NULL,
    preco REAL NOT NULL
);

CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY, 
    nome TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE Historico (
    id INTEGER PRIMARY KEY,
    usuario_id INTEGER,
    livro_id INTEGER,
    acao TEXT,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id),
    FOREIGN KEY (livro_id) REFERENCES Livros(id)
);

INSERT INTO Livros (id,titulo, autor, genero, preco) VALUES
('01', 'O Alquimista', 'Paulo Coelho', 'Aventura', 30.00),
('02','1984', 'George Orwell', 'Distopia', 25.00),
('03', 'O Senhor dos Anéis', 'J.R.R. Tolkien', 'Fantasia', 50.00);

INSERT INTO Usuarios (id,nome, email) VALUES
('10' , 'João', 'joao@email.com'),
(11, 'Maria','maria@email.com');

INSERT INTO Historico (id, usuario_id, livro_id, acao) 
VALUES (20, 10, 2, 'Reservado'), (21, 11, 1, 'Comprado');

SELECT * FROM Livros;
SELECT * FROM Usuarios;
SELECT * FROM Historico;