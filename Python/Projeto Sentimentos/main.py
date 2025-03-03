import json
from noticias import obter_noticias
from processamento import limpar_texto
from analise import analisar_sentimentos

def calcular_sentimento_medio(sentimentos):
    soma = sum(s.get("document", {}).get("score", 0) for s in sentimentos if "document" in s)
    return soma / len(sentimentos) if sentimentos else 0

def main():
    tema = input("Digite o tema para buscar notícias: ")
    noticias = obter_noticias(tema)
    resultados = []
    sentimentos = []
    
    for noticia in noticias:
        titulo = noticia.get("title", "Sem título")
        descricao = noticia.get("description", "Sem descrição")
        texto_limpo = limpar_texto(titulo + " " + descricao)
        
        if not texto_limpo:
            continue 
        
        sentimento, emocao = analisar_sentimentos(texto_limpo)
        sentimentos.append(sentimento)
        
        resultado = {
            "titulo": titulo,
            "descricao": descricao,
            "sentimento": sentimento,
            "emocoes": emocao
        }
        resultados.append(resultado)
        print(f"Notícia: {titulo} | Sentimento: {sentimento.get('document', {}).get('label', 'desconhecido')}")
    
    sentimento_medio = calcular_sentimento_medio(sentimentos)
    print(f"\nSentimento médio das notícias: {sentimento_medio:.2f}")
    
    with open("resultados.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)
    
    print("\nAnálise concluída! Resultados salvos em 'resultados.json'")

if __name__ == "__main__":
    main()