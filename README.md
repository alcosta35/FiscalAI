\# FiscalAI - Auditor Fiscal Inteligente



Sistema inteligente para auditoria fiscal usando IA.



\## 🚀 Executar no Google Colab



1\. Abra o notebook: \[FiscalAI\_Colab.ipynb](link\_to\_your\_colab\_notebook)

2\. Execute as células em ordem

3\. Faça upload dos arquivos CSV quando solicitado



\## 📋 Requisitos



\- Python 3.10+

\- OpenAI API Key



\## 📁 Estrutura do Projeto

```

FiscalAI/

├── config.py          # Configurações

├── main.py            # FastAPI app

├── agente\_cfop.py     # Agente validador

├── models/            # Modelos Pydantic

├── routes/            # Endpoints da API

└── services/          # Lógica de negócio

```



\## 🔑 Configuração



Criar arquivo `.env` com:

```

OPENAI\_API\_KEY=sk-...

```

