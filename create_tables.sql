CREATE TABLE exames_realizados (

    unidade VARCHAR(200),

    nome VARCHAR(255),

    funcao VARCHAR(255),

    setor VARCHAR(100),

    exame VARCHAR(255),

    data_exame DATE
);

CREATE TABLE funcoes_ghe (
    unidade VARCHAR(200),
    setor VARCHAR(100),
    funcao VARCHAR(255),
    ghe INT
);

CREATE TABLE ghe_exames (
    unidade VARCHAR(200),
    ghe INT,
    exame VARCHAR(255),
    admissional BOOLEAN,
    periodico BOOLEAN,
    demissional BOOLEAN
);
