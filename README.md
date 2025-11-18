# tlj-video-notes 🎥📝  
Ferramenta em Python para **gerar notas, resumos e marcadores de vídeos**, a partir de links e trechos específicos.

---

## 🎯 O que esse projeto faz?

- Extrai informações de vídeos (YouTube ou arquivo local – conforme evolução)  
- Gera **notas organizadas** a partir de um intervalo de tempo  
- Permite registrar **timestamps importantes**  
- Oferece uma experiência simples via **linha de comando (CLI)**  
- Mostra código organizado e legível para recrutadores

---

## 🧱 Estrutura do Projeto

```bash
tlj-video-notes/
├── main.py            # Ponto de entrada da aplicação (CLI)
├── models_memory.py   # Modelos / estrutura dos dados em memória
├── schemas.py         # Esquemas / tipos usados na aplicação
├── __pycache__/       # Arquivos compilados (Python)
├── .venv/             # Ambiente virtual (ignorável no Git)
└── README.md

🛠️ Tecnologias Utilizadas
Tecnologia	Uso
🐍 Python 3.10+	Linguagem principal
Rich / libs CLI	Interface mais amigável no terminal
(Evolução futura) moviepy, pytube	Para extração de dados de vídeo
Modularização	Código separado por responsabilidade
▶️ Como usar

Clonar o repositório

git clone https://github.com/BrunoApMarques/tlj-video-notes.git
cd tlj-video-notes


Criar/ativar ambiente virtual (opcional, mas recomendado)

python -m venv .venv
source .venv/Scripts/activate  # Windows (Git Bash)
# ou
source .venv/bin/activate      # Linux/Mac


Instalar dependências (quando o requirements.txt estiver configurado)

pip install -r requirements.txt


Executar o script

python main.py

🧪 Exemplo de fluxo (conceitual)

Entrada no terminal:

Link do vídeo: https://youtube.com/xxxxx

Horário inicial: 00:00:00

Horário final: 00:05:12

Saída (exemplo em JSON):

{
  "video": "Como funciona uma API REST",
  "notas": [
    "API é um meio de comunicação entre sistemas",
    "REST utiliza padrões HTTP",
    "É stateless e escalável"
  ],
  "duracao_analisada": "00:00:00 → 00:05:12"
}

🚀 Roadmap (Evoluções Futuras)

 Suporte a download automático do vídeo

 Criar interface gráfica (Tkinter, PyQt ou web)

 Integração com ferramentas de IA (ex.: transcrição automática)

 Exportar notas em PDF / Markdown