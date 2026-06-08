# auditoria-asos-python
Automação de auditoria de ASOs utilizando Python, PostgreSQL e análise de dados.

## Sobre o Projeto

Este projeto tem como objetivo automatizar a auditoria de exames ocupacionais por meio da extração e tratamento de dados contidos em ASOs (Atestados de Saúde Ocupacional).

A solução foi desenvolvida para reduzir o tempo gasto em conferências manuais e aumentar a confiabilidade do processo de auditoria.

## Problema

A auditoria dos exames ocupacionais era realizada de forma predominantemente manual, exigindo a análise individual de centenas de ASOs e o confronto das informações contidas nos documentos com a matriz de exames obrigatórios definida para cada cargo e função.

Esse processo demandava um elevado volume de trabalho operacional, consumia muitas horas de conferência e aumentava o risco de inconsistências, especialmente em auditorias com grande quantidade de colaboradores. A necessidade de verificar manualmente quais exames haviam sido realizados e identificar eventuais pendências tornava o acompanhamento da conformidade ocupacional lento e pouco escalável.

## Solução Desenvolvida

O projeto realiza:

Extração de informações de ASOs em PDF;
Padronização e tratamento dos dados utilizando Python;
Armazenamento das informações em PostgreSQL;
Relacionamento entre funcionários, cargos e exames obrigatórios;
Identificação automática de exames pendentes ou não realizados.

## Tecnologias

Python
Pandas
PostgreSQL
SQL
PDFPlumber
Regex
Git e GitHub

## Estrutura do Projeto

dados/ – arquivos utilizados durante o desenvolvimento;
notebooks/ – análises exploratórias e testes;
src/ – scripts principais do projeto;
sql/ – consultas e scripts de banco de dados;
imagens/ – diagramas e fluxos do projeto.
