# VoxNLP - Comunicação Aumentativa com IA (v1)

VoxNLP é uma aplicação assistiva que utiliza inteligência artificial para apoiar a comunicação em tempo real por meio de **recomendações textuais inteligentes**. O projeto é voltado a pessoas com deficiência auditiva, autismo ou dificuldades de atenção, especialmente em contextos de reuniões online.

---

## 🚀 Principais Funcionalidades

- 🎙️ **Transcrição de Áudio com Whisper**
- 💬 **Recomendação de palavras com BERTimbau e Trie**
- 🧠 **Modo híbrido**: sugestões baseadas em frequência e similaridade contextual
- ⌨️ Integração com **teclado virtual**
- ⚡ Backend com **FastAPI + WebSocket** para resposta em tempo real

---

## 🧩 Estrutura do Projeto
```bash
VoxNLP/
├── app/
│ ├── api/ # Endpoints da API (REST e WebSocket)
│ ├── core/ # Módulos de transcrição e recomendação
│ ├── models/ # Schemas e validações
│ ├── services/ # Redis handler e serviços auxiliares
│ ├── tests/ # Testes unitários
│ ├── config.py # Configurações globais
│ └── main.py # Inicialização do FastAPI
├── client/
│ ├── voxnlp_client_streamlit.py # Interface via Streamlit
│ ├── client_voxnlp.py # Cliente WebSocket de exemplo
├── data/
│ └── samples/ # Arquivos de áudio de exemplo
├── requirements.txt
├── Dockerfile
└── README.md
```
---

## ⚙️ Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/voxnlp.git
cd voxnlp
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Executar o pipeline (uma única vez):

```bash
python executar_pipeline.py      # Linux/macOS
python.exe executar_pipeline.py  # Windows
```

5. Iniciar o backend FastAPI:

```bash
uvicorn api:app --reload
```
Acesse: http://127.0.0.1:8000/docs para a documentação automática da API.

6. Executar o cliente Streamlit (opcional):

```bash
streamlit run client/voxnlp_client_streamlit.py
```

Autor
Fernando Torres Ferreira da Silva
Mestrando no ICMC/USP – Inteligência Artificial & Acessibilidade
Idealizador da comunidade Data Science Enthusiasts

Citação (se aplicável)
Se este projeto for útil para seu trabalho acadêmico ou pesquisa, por favor cite:

bibtex

```bash
@misc{torres2025voxnlp,
  author = {Torres, Fernando},
  title = {VoxNLP: Comunicação Aumentativa com IA e NLP em Reuniões Online},
  year = {2025},
  howpublished = {\url{https://github.com/seu-usuario/voxnlp}}
}
```
