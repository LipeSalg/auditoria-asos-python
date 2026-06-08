-- Identifica exames obrigatórios que não foram encontrados
-- nos ASOs processados para cada colaborador.

SELECT
    fg.unidade,
    fg.ghe,
    er.nome,
    er.funcao,
    ge.exame AS exame_faltante

FROM pcmso.exames_realizados er

-- Relaciona a função do colaborador ao GHE
INNER JOIN pcmso.funcoes_ghe fg
    ON er.funcao = fg.funcao
   AND er.unidade = fg.unidade

-- Obtém os exames obrigatórios do GHE
INNER JOIN pcmso.ghe_exames ge
    ON fg.ghe = ge.ghe
   AND fg.unidade = ge.unidade

-- Verifica se o exame obrigatório foi encontrado
LEFT JOIN pcmso.exames_realizados er2
    ON er2.nome = er.nome
   AND er2.exame = ge.exame
   AND er2.unidade = ge.unidade
-- Filtro para ver o tipo de exame, se é admissional, demissional, periódico
WHERE er2.exame IS NULL
  AND ge.demissional = TRUE

ORDER BY
    fg.unidade,
    fg.ghe,
    er.nome;
