import re
import unicodedata


def normalizar(texto):

    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    texto = texto.upper()

    texto = re.sub(r'\s+', ' ', texto)

    return texto.strip()
