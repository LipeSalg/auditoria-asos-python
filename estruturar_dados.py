import pandas as pd


def estruturar_dados(dados):

    registros = []

    for funcionario in dados:

        unidade = funcionario["unidade"]
        nome = funcionario["nome"]

        funcao_completa = funcionario["funcao"]

        if "SETOR / SECTION:" in funcao_completa:

            partes = funcao_completa.split(
                "SETOR / SECTION:"
            )

            funcao = partes[0].strip()
            setor = partes[1].strip()

        else:

            funcao = funcao_completa.strip()
            setor = ""

        for exame in funcionario["exames"]:

            data = exame["data"]

            data_formatada = (
                data.split('/')[2] + '-' +
                data.split('/')[1] + '-' +
                data.split('/')[0]
            )

            registros.append({

                "unidade": unidade,

                "nome": nome,

                "funcao": funcao,

                "setor": setor,

                "exame": exame["exame"],

                "data_exame": data_formatada
            })

    df = pd.DataFrame(registros)

    return df
