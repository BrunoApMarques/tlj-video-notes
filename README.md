# TLJ Video Notes (FastAPI)

API em **Python + FastAPI** para praticar conceitos básicos (Git, Linux/Bash, REST, testes, documentação).  
Começa com um endpoint de _health check_ e será evoluída para registrar **anotações de vídeos** (tópicos/trechos marcados, tags, etc.).

##Estrutura do projeto

tlj-video-notes/
├── app/
│   ├── main.py            # App FastAPI + rotas
│   ├── schemas.py         # Pydantic models (serão usados nas próximas features)
│   └── models_memory.py   # "Storage" em memória (será substituído por DB futuramente)
├── .gitignore
└── README.md


## Stack
- Python 3.9+
- FastAPI
- Uvicorn (dev server)

## Como rodar localmente

### 1) Clonar e entrar na pasta
bashh
git clone https://github.com/BrunoApMarques/tlj-video-notes.git
cd tlj-video-notes
