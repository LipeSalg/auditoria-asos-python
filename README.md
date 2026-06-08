# auditoria-asos-python
Automação de auditoria de ASOs utilizando Python, PostgreSQL e análise de dados.

## Sobre o Projeto

Este projeto tem como objetivo automatizar a auditoria de exames ocupacionais por meio da extração e tratamento de dados contidos em ASOs (Atestados de Saúde Ocupacional).

A solução foi desenvolvida para reduzir o tempo gasto em conferências manuais e aumentar a confiabilidade do processo de auditoria.

## Problema

A auditoria dos exames ocupacionais era realizada de forma predominantemente manual, exigindo a análise individual de centenas de ASOs e o confronto das informações contidas nos documentos com a matriz de exames obrigatórios definida para cada cargo e função.

Esse processo demandava um elevado volume de trabalho operacional, consumia muitas horas de conferência e aumentava o risco de inconsistências, especialmente em auditorias com grande quantidade de colaboradores. A necessidade de verificar manualmente quais exames haviam sido realizados e identificar eventuais pendências tornava o acompanhamento da conformidade ocupacional lento e pouco escalável.


## Fonte dos dados

A matriz de exames ocupacionais utilizada no projeto foi disponibilizada originalmente em formato PDF, contendo a relação entre funções e os respectivos exames obrigatórios.

Para possibilitar a automação da auditoria, os dados foram extraídos, estruturados e padronizados em formato tabular, permitindo sua utilização em consultas SQL e validações automatizadas.

## Regras de Negócio

Cada função possui uma relação específica de exames obrigatórios definida pela matriz ocupacional.

O processo de auditoria consiste em:

1. Identificar a função do colaborador.
2. Consultar os exames obrigatórios para a função.
3. Verificar os exames realizados pelo colaborador.
4. Comparar os exames realizados com os exames exigidos.
5. Identificar pendências ou não conformidades.

Exemplo:

Função: Motorista

Exames obrigatórios:
- Clínico Ocupacional
- Audiometria

Resultado da auditoria:
- Clínico Ocupacional: OK
- Audiometria: Pendente

## Solução Desenvolvida

A solução automatiza o processo de auditoria através das seguintes etapas:

- Extração de dados dos ASOs em PDF;
- Tratamento e padronização das informações;
- Armazenamento em PostgreSQL;
- Relacionamento entre colaboradores, funções e exames obrigatórios;
- Identificação automática de pendências;
- Geração de relatórios para acompanhamento da conformidade ocupacional

## Resultados

A solução automatizou a auditoria de exames ocupacionais por meio de:

- Leitura automática de ASOs em PDF;
- Extração de informações utilizando OCR;
- Identificação de função, setor e exames realizados;
- Estruturação dos dados em PostgreSQL;
- Relacionamento entre Função, GHE e Exames Obrigatórios;
- Identificação automática de exames pendentes através de views SQL.

## Tecnologias

- Python
- Pandas
- PostgreSQL
- SQL
- Regex
- Unidecode
- Git e GitHub
- PDF2Image
- Tesseract OCR
- PyTesseract
- Google Colab

## Estrutura do Projeto

- dados/ – arquivos utilizados durante o desenvolvimento;
- notebooks/ – análises exploratórias e testes;
- src/ – scripts principais do projeto;
- sql/ – consultas e scripts de banco de dados;
- imagens/ – diagramas e fluxos do projeto.
