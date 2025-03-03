from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def analisar_sentimentos(texto):
    IBM_API_KEY = "d0ffab5b13a24a458c9eb19be17f3619"
    IBM_API_URL = "https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com"
    
    try:
        autenticador = IAMAuthenticator(IBM_API_KEY)
        nlu = NaturalLanguageUnderstandingV1(version="2021-08-01", authenticator=autenticador)
        nlu.set_service_url(IBM_API_URL)
        resposta = nlu.analyze(text=texto, features=Features(sentiment=SentimentOptions(), emotion=EmotionOptions())).get_result()
        return resposta.get("sentiment", {}), resposta.get("emotion", {})
    except Exception as e:
        print(f"Erro ao analisar sentimentos: {e}")
        return {"document": {"label": "desconhecido", "score": 0}}, {}