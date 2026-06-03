CREATE DATABASE IF NOT EXISTS gerenciamento_estoque;
USE gerenciamento_estoque;

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome       VARCHAR(100) NOT NULL,
    email      VARCHAR(50)  UNIQUE NOT NULL,
    senha      VARCHAR(255) NOT NULL,
    perfil     ENUM('ADMIN', 'OPERADOR') NOT NULL
);

CREATE TABLE produtos (
    id_produto         INT AUTO_INCREMENT PRIMARY KEY,
    nome               VARCHAR(150)   NOT NULL,
    descricao          TEXT,
    preco              DECIMAL(10,2)  NOT NULL,
    quantidade_estoque INT            DEFAULT 0,
    localizacao        VARCHAR(100)
);

CREATE TABLE entradas_estoque (
    id_entrada   INT AUTO_INCREMENT PRIMARY KEY,
    id_produto   INT NOT NULL,
    quantidade   INT NOT NULL,
    data_entrada DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_entrada_produto
        FOREIGN KEY (id_produto)
        REFERENCES produtos(id_produto)
);

CREATE TABLE saidas_estoque (
    id_saida   INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    data_saida DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_saida_produto
        FOREIGN KEY (id_produto)
        REFERENCES produtos(id_produto)
);