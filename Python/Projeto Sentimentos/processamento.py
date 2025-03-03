import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")
stop_words = set(stopwords.words("portuguese"))

def limpar_texto(texto):
    if not isinstance(texto, str) or not texto.strip():
        return ""
    tokens = word_tokenize(texto.lower())
    return " ".join([palavra for palavra in tokens if palavra.isalnum() and palavra not in stop_words])