from  unidecode import unidecode
import re

def sanitizar(texto):
    texto = unidecode(texto)
    texto = texto.lower()
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()

    return texto