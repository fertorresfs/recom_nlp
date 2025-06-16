# ============================================
# Autor: Fernando Torres Ferreira da Silva
# Projeto: RecomNLP
# Versão: 1.0
# Arquivo: executar_pipeline.py
# Data: 15/06/2025
# ============================================

import os
from transformers import AutoTokenizer, AutoModel
from preprocessamento import (
    baixar_e_preparar_frequencia,
    preparar_vocab_e_trie,
    calcular_embeddings,
    carregar_dispositivo
)

# CONFIGS
#BERTimbau da NeuralMind https://huggingface.co/neuralmind/bert-base-portuguese-cased
BERT_MODEL_NAME = "neuralmind/bert-base-portuguese-cased"
ARQUIVO_LEXICO = "lexporbr_alfa_txt.txt" 
MAX_PALAVRAS = 3000 
BATCH_SIZE = 32

def main():
    print("INÍCIO DO PIPELINE")

    # 1. Baixando e Preparando a Frequência
    if not os.path.exists("frequencia.pkl"):
        baixar_e_preparar_frequencia(ARQUIVO_LEXICO)
    else:
        print("[PULADO] Frequência já processada.")

    # 2. Carregando o modelo BERT Tokenizer e Modelo
    print("[INFO] Carregando modelo BERT...")
    tokenizer = AutoTokenizer.from_pretrained(BERT_MODEL_NAME)
    model = AutoModel.from_pretrained(BERT_MODEL_NAME)

    # 3. Criando Vocabulário e Trie
    if not os.path.exists("trie.pkl") or not os.path.exists("vocabulario.pkl"):
        vocabulario = preparar_vocab_e_trie(tokenizer, MAX_PALAVRAS)
    else:
        print("[PULADO] Trie e vocabulário já existem.")
        import pickle
        with open("vocabulario.pkl", "rb") as f:
            vocabulario = pickle.load(f)

    # 4. Calculo e Geração dos Embeddings
    if not os.path.exists("embeddings.npy"):
        dispositivo = carregar_dispositivo()
        calcular_embeddings(vocabulario, tokenizer, model, BATCH_SIZE, dispositivo)
    else:
        print("[PULADO] Embeddings já gerados.")

    print("PIPELINE CONCLUÍDO")

if __name__ == "__main__":
    main()
