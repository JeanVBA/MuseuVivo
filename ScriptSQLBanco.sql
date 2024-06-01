-- Table structure for table `instituicoes`
DROP TABLE IF EXISTS instituicoes;
CREATE TABLE instituicoes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL
);

-- Table structure for table `localizacoes`
DROP TABLE IF EXISTS localizacoes;
CREATE TABLE localizacoes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL
);

-- Table structure for table `guias`
DROP TABLE IF EXISTS guias;
CREATE TABLE guias (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  telefone VARCHAR(20)
);

-- Table structure for table `visitas_guiadas`
DROP TABLE IF EXISTS visitas_guiadas;
CREATE TABLE visitas_guiadas (
  id SERIAL PRIMARY KEY,
  grupo VARCHAR(255),
  data_visita DATE,
  horario TIME,
  guia_responsavel_id INTEGER,
  FOREIGN KEY (guia_responsavel_id) REFERENCES guias(id)
);

-- Table structure for table `pinturas`
DROP TABLE IF EXISTS pinturas;
CREATE TABLE pinturas (
  id SERIAL PRIMARY KEY,
  obra_id INTEGER,
  tecnica VARCHAR(100),
  FOREIGN KEY (obra_id) REFERENCES obras(id) ON DELETE CASCADE
);

-- Table structure for table `emprestimos`
DROP TABLE IF EXISTS emprestimos;
CREATE TABLE emprestimos (
  id SERIAL PRIMARY KEY,
  obra_id INTEGER,
  data_emprestimo DATE,
  data_retorno DATE,
  instituicao_id INTEGER,
  FOREIGN KEY (obra_id) REFERENCES obras(id),
  FOREIGN KEY (instituicao_id) REFERENCES instituicoes(id)
);

-- Table structure for table `esculturas`
DROP TABLE IF EXISTS esculturas;
CREATE TABLE esculturas (
  id SERIAL PRIMARY KEY,
  obra_id INTEGER,
  material VARCHAR(100),
  peso DECIMAL(10, 2),
  FOREIGN KEY (obra_id) REFERENCES obras(id) ON DELETE CASCADE
);

-- Table structure for table `obras_exposicoes`
DROP TABLE IF EXISTS obras_exposicoes;
CREATE TABLE obras_exposicoes (
  obra_id INTEGER,
  exposicao_id INTEGER,
  PRIMARY KEY (obra_id, exposicao_id),
  FOREIGN KEY (exposicao_id) REFERENCES exposicoes(id),
  FOREIGN KEY (obra_id) REFERENCES obras(id)
);

-- Table structure for table `exposicoes`
DROP TABLE IF EXISTS exposicoes;
CREATE TABLE exposicoes (
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  descricao TEXT,
  data_inicio DATE,
  data_termino DATE
);

-- Table structure for table `autores`
DROP TABLE IF EXISTS autores;
CREATE TABLE autores (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL
);

-- Table structure for table `segurancas`
DROP TABLE IF EXISTS segurancas;
CREATE TABLE segurancas (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  telefone VARCHAR(20),
  localizacao_id INTEGER,
  FOREIGN KEY (localizacao_id) REFERENCES localizacoes(id)
);

-- Table structure for table `ingressos`
DROP TABLE IF EXISTS ingressos;
CREATE TABLE ingressos (
  id SERIAL PRIMARY KEY,
  visitante_id INTEGER,
  tipo VARCHAR(50),
  data_visita DATE,
  visita_guiada_id INTEGER,
  FOREIGN KEY (visita_guiada_id) REFERENCES visitas_guiadas(id),
  FOREIGN KEY (visitante_id) REFERENCES visitantes(id)
);

-- Table structure for table `obras`
DROP TABLE IF EXISTS obras;
CREATE TABLE obras (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  descricao TEXT,
  data_criacao DATE,
  autor_id INTEGER,
  localizacao_id INTEGER,
  tipo VARCHAR(50),
  FOREIGN KEY (autor_id) REFERENCES autores(id),
  FOREIGN KEY (localizacao_id) REFERENCES localizacoes(id)
);

-- Table structure for table `visitantes`
DROP TABLE IF EXISTS visitantes;
CREATE TABLE visitantes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  telefone VARCHAR(20)
);
