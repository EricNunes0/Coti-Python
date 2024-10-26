-- Acesso ao banco de dados POSTGRESQL
-- SQL SHELL -> Informar a senha do banco
-- Senha local -> coti

-- Remover uma base de dados
DROP DATABASE aulap;

-- Criação da base de dados
CREATE DATABASE aulap;

-- Conectar a base de dados
\c aulap

-- Criação da tabela do projeto
-- Produto -> codigo, nome, preco, quantidade
CREATE TABLE produto(
    codigo serial primary key,
    nome varchar(50) not null,
    preco decimal not null,
    quantidade integer not null
);

-- Exibir os objetos do banco de dados
\d

-- Descrever o objeto do banco de dados
\d produto

-- Inserir dados na tabela
--  INSERT INTO produto;
INSERT INTO produto(nome, preco, quantidade) VALUES ('Mouse', 120.00, 10);
INSERT INTO produto(nome, preco, quantidade) VALUES ('Monitor 15 LCD', 400.00, 8);
INSERT INTO produto(nome, preco, quantidade) VALUES ('Teclado Microsoft', 50.00, 4);
INSERT INTO produto(nome, preco, quantidade) VALUES ('Playstation 5 Pro', 8000.00, 7);
INSERT INTO produto(nome, preco, quantidade) VALUES ('Xbox One', 800.00, 3);
INSERT INTO produto(nome, preco, quantidade) VALUES ('Playstation 2', 500.00, 13);
INSERT INTO produto(nome, preco, quantidade) VALUES ('Super Nintendo', 550.00, 9);
INSERT INTO produto(nome, preco, quantidade) VALUES ('Mega Drive', 400.00, 10);

-- Seleção, consultas
SELECT codigo, nome FROM produto;
SELECT * FROM produto;

-- Delete -> Filtro, WHERE (campo)
DELETE FROM produto WHERE codigo = 7;

-- Update, atualização
UPDATE produto set nome = 'Game Boy Advance' WHERE codigo = 8;