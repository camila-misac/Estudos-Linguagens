import requests

def obter_noticias(tema):
    NEWS_API_KEY = "d0ffab5b13a24a458c9eb19be17f3619"
    NEWS_API_URL = "https://newsapi.org/v2/everything"
    
    parametros = {"q": tema, "apiKey": NEWS_API_KEY, "language": "pt", "pageSize": 10}
    resposta = requests.get(NEWS_API_URL, params=parametros)
    
    if resposta.status_code != 200:
        print("Erro ao acessar NewsAPI:", resposta.status_code, resposta.text)
        return []
    
    dados = resposta.json()
    return dados.get("articles", [])
