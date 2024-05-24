CREATE DATABASE MuseuVivo;
USE MuseuVivo;

-- Tabela para localizações
CREATE TABLE Localizacoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL
);
-- Tabela para Auto
CREATE TABLE Autores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL
);

-- Tabela para obras de arte
CREATE TABLE Obras (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_criacao DATE,
    autor_id INT,
    localizacao_id INT,
    tipo VARCHAR(50),
    FOREIGN KEY (autor_id) REFERENCES Autores(id),
    FOREIGN KEY (localizacao_id) REFERENCES Localizacoes(id)
);


-- Tabela para esculturas (herdando de ObrasArte)
CREATE TABLE Esculturas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    obra_id INT,
    material VARCHAR(100),
    peso DECIMAL(10, 2),
    FOREIGN KEY (obra_id) REFERENCES Obras(id) ON DELETE CASCADE
);

CREATE TABLE Pinturas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    obra_id INT,
    tecnica VARCHAR(100),
    FOREIGN KEY (obra_id) REFERENCES Obras(id) ON DELETE CASCADE
);

-- Tabela para exposições temporárias
CREATE TABLE Exposicoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_inicio DATE,
    data_termino DATE
);

-- Tabela para empréstimos de obras de arte
CREATE TABLE Emprestimos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    obra_id INT,
    data_emprestimo DATE,
    data_retorno DATE,
    instituicao_solicitante VARCHAR(255),
    FOREIGN KEY (obra_id) REFERENCES Obras(id)
);

-- Tabela para visitantes
CREATE TABLE Visitantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telefone VARCHAR(20)
);

-- Tabela para ingressos
CREATE TABLE Ingressos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    visitante_id INT,
    tipo VARCHAR(50),
    data_visita DATE,
    visita_guiada_id INT,
    FOREIGN KEY (visitante_id) REFERENCES Visitantes(id),
    FOREIGN KEY (visita_guiada_id) REFERENCES Visitas_Guiadas(id)
);

-- Tabela para visitas guiadas
CREATE TABLE Visitas_Guiadas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    grupo VARCHAR(255),
    data_visita DATE,
    horario TIME,
    guia_responsavel_id INT,
    FOREIGN KEY (guia_responsavel_id) REFERENCES Guias(id)
);

-- Tabela para guias responsáveis
CREATE TABLE Guias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telefone VARCHAR(20)
);

-- Tabela de associação entre ObrasArte e Exposicoes (Many-to-Many)
CREATE TABLE Obras_Exposicoes (
    obra_id INT,
    exposicao_id INT,
    PRIMARY KEY (obra_id, exposicao_id),
    FOREIGN KEY (obra_id) REFERENCES Obras(id),
    FOREIGN KEY (exposicao_id) REFERENCES Exposicoes(id)
);

-- Tabela para seguranças
CREATE TABLE Segurancas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telefone VARCHAR(20),
    localizacao_id INT,
    FOREIGN KEY (localizacao_id) REFERENCES Localizacoes(id)
);
