import os
import re

from pdf2image import convert_from_path
import pytesseract

from tratamento_texto import normalizar


def processar_asos(pasta, exames):

    lista_funcionarios = []

    for arquivo in os.listdir(pasta):

        if arquivo.lower().endswith(".pdf"):

            caminho_pdf = os.path.join(
                pasta,
                arquivo
            )

            nome_arquivo = os.path.splitext(
                arquivo
            )[0]

            nome_arquivo = re.sub(
                r'\s*\(\d+\)',
                '',
                nome_arquivo
            )

            paginas = convert_from_path(
                caminho_pdf
            )

            texto_total = ""

            for pagina in paginas:

                texto = pytesseract.image_to_string(
                    pagina,
                    lang="por"
                )

                texto_total += texto

            texto_total = normalizar(
                texto_total
            )

            funcao = re.search(
                r'FUNCAO \/ FUNCTION:\s*(.*)',
                texto_total
            )

            funcao_funcionario = (
                funcao.group(1).strip()
                if funcao else ''
            )

            exames_encontrados = []

            datas = []

            for exame in exames:

                exame_norm = normalizar(
                    exame
                )

                padrao = (
                    rf'{exame_norm}'
                    rf'[\s\S]{{0,80}}?'
                    rf'(\d{{2}}/\d{{2}}/\d{{4}})'
                )

                resultado = re.search(
                    padrao,
                    texto_total
                )

                if resultado:

                    data_exame = resultado.group(1)

                    exames_encontrados.append({
                        "exame": exame,
                        "data": data_exame
                    })

                    datas.append(
                        data_exame
                    )

            dados_funcionario = {

                "unidade": codigo_unidade,

                "nome": nome_arquivo,

                "funcao": funcao_funcionario,

                "datas_exames": list(
                    set(datas)
                ),

                "exames": exames_encontrados
            }

            lista_funcionarios.append(
                dados_funcionario
            )

    return lista_funcionarios
