import os
from pdf2image import convert_from_path
import pytesseract


def extrair_texto_pdfs(pasta):

    texto_total = ""

    for arquivo in os.listdir(pasta):

        if arquivo.lower().endswith(".pdf"):

            caminho_pdf = os.path.join(
                pasta,
                arquivo
            )

            print(f"Lendo: {arquivo}")

            paginas = convert_from_path(
                caminho_pdf
            )

            texto_total += (
                f"\n\n===== {arquivo} =====\n\n"
            )

            for pagina in paginas:

                texto = pytesseract.image_to_string(
                    pagina,
                    lang="por"
                )

                texto_total += texto

    return texto_total
