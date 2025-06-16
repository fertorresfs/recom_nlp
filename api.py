# ============================================
# Autor: Fernando Torres Ferreira da Silva
# Projeto: RecomNLP
# Versão: 1.0
# Arquivo: api.py
# Data: 15/06/2025
# ============================================

from fastapi import FastAPI, Query
import uvicorn
import pickle
import numpy as np
from typing import List
from preprocessamento import (gerar_sugestoes_gpt2,
    sugerir_hibrido)

app = FastAPI(title="API de Recomendação de Palavras", version="1.0")

# Carregamento dos recursos
with open("trie.pkl", "rb") as f:
    trie = pickle.load(f)

with open("vocabulario.pkl", "rb") as f:
    vocabulario = pickle.load(f)

with open("frequencia.pkl", "rb") as f:
    frequencia = pickle.load(f)

embeddings = np.load("embeddings.npy")


# Endpoints

@app.get("/sugestoes/", summary="Sugestões com base no prefixo")
def sugerir(prefixo: str = Query(..., min_length=1), limite: int = 5):
    """Sugere palavras que começam com o prefixo fornecido."""
    prefixo = prefixo.lower()
    
    if not trie.has_subtrie(prefixo):
        return {"prefixo": prefixo, "sugestoes": []}

    candidatos = list(trie.iterkeys(prefixo))
    candidatos = sorted(candidatos, key=lambda p: frequencia.get(p, 1.0), reverse=True)
    
    return {"prefixo": prefixo, "sugestoes": candidatos[:limite]}

#@app.get("/sugestoes/", summary="Sugestões com base no prefixo")
#def sugerir(prefixo: str = Query(..., min_length=1), limite: int = 5):
#    """Sugere palavras que começam com o prefixo fornecido."""
#    candidatos = list(trie.iterkeys(prefixo.lower()))
#    candidatos = sorted(candidatos, key=lambda p: frequencia.get(p, 1.0), reverse=True)
#    return {"prefixo": prefixo, "sugestoes": candidatos[:limite]}


@app.get("/embedding/", summary="Retorna o embedding de uma palavra")
def get_embedding(palavra: str):
    """Retorna o vetor de embedding da palavra, se existir no vocabulário."""
    palavra = palavra.lower()
    try:
        idx = vocabulario.index(palavra)
        vetor = embeddings[idx].tolist()
        return {"palavra": palavra, "embedding": vetor}
    except ValueError:
        return {"erro": f"A palavra '{palavra}' não está no vocabulário."}


@app.get("/frequencia/", summary="Consulta a frequência estimada de uma palavra")
def get_frequencia(palavra: str):
    """Consulta a frequência aproximada da palavra (quanto menor, mais frequente)."""
    palavra = palavra.lower()
    freq = frequencia.get(palavra)
    if freq:
        return {"palavra": palavra, "frequencia_invertida": freq}
    return {"erro": f"Palavra '{palavra}' não encontrada no léxico."}

@app.get("/sugestoes_gpt2/", summary="Sugestões com GPT-2")
def sugerir_com_gpt2(prefixo: str = Query(..., min_length=1), limite: int = 5):
    sugestoes = gerar_sugestoes_gpt2(prefixo, num_sugestoes=limite)
    completas = [f"{prefixo}{s}" for s in sugestoes]
    return {"prefixo": prefixo, "sugestoes": completas}

@app.get("/sugestoes_hibrido/", summary="Sugestões com Trie + GPT-2")
def endpoint_sugestoes(prefixo: str = Query(..., min_length=1), limite: int = 5):
    sugestoes = sugerir_hibrido(prefixo, limite)
    return {"prefixo": prefixo, "sugestoes": sugestoes}


# Execução local
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
