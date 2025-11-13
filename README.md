🎥 tlj-video-notes — Extração Inteligente de Notas de Vídeos (Python)



Ferramenta simples em Python que permite ao usuário gerar notas, resumos e marcadores de vídeos a partir de links, timestamps ou trechos específicos.

É ideal para estudantes, criadores de conteúdo e para treinar Python de forma prática e moderna.

🧠 O que esse projeto faz?

✔ Extrai informações de vídeos (YouTube ou arquivo local)
✔ Gera notas organizadas
✔ Permite adicionar timestamps
✔ Oferece uma experiência simples de uso pelo terminal (CLI)
✔ Código limpo e fácil de entender (ótimo para recrutadores)

📁 Estrutura do Projeto


tlj-video-notes/

 ├── main.py               # Ponto de entrada da aplicação
 ├── extractor.py          # Módulo responsável por extrair infos
 ├── notes_generator.py    # Gera notas e resumo
 ├── utils.py              # Funções auxiliares
 └── README.md


🚀 Tecnologias Utilizadas

Tecnologia	Uso
🐍 Python 3.10+	Linguagem principal
🎞 moviepy / pytube	Extração de dados do vídeo
📝 Rich (CLI Bonito)	Formatação colorida no terminal
🧩 Modularização	Código organizado por responsabilidade


▶️ Como usar
1️⃣ Clonar o repositório
git clone https://github.com/BrunoApMarques/tlj-video-notes.git
cd tlj-video-notes

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Executar o script
python main.py

📝 Exemplo de uso
Entrada:
Digite o link do vídeo:
https://youtube.com/xxxxx

Digite o horário inicial (ex: 00:01:23):
00:00:00

Digite o horário final (ex: 00:03:40):
00:05:12


Saída gerada:


{
  "video": "Como funciona uma API REST",
  "notas": [
    "API é um meio de comunicação entre sistemas",
    "REST utiliza padrões HTTP",
    "É stateless e escalável"
  ],
  "duracao_analisada": "00:00:00 → 00:05:12"
}

🗺 Roadmap (Evolução futura)

Adicionar suporte a download automático

Criar interface gráfica (Tkinter ou PyQt)

Integração com IA (OpenAI Whisper)

Exportar notas em PDF


👨‍💻 Autor

Bruno Marques
Desenvolvedor Back-end (Java + Python)
🔗 GitHub: https://github.com/BrunoApMarques
