<<<<<<< HEAD
📌 Real-Time Payment App
💰 Aplicação Flask para pagamentos em tempo real com PIX e WebSockets.

📜 Descrição
Este projeto é uma aplicação Flask que simula pagamentos via PIX em tempo real. Ele utiliza Flask-SocketIO para comunicação em tempo real e Flask-SQLAlchemy para gerenciamento do banco de dados.

🚀 Tecnologias Utilizadas
Python 3.10+
Flask
Flask-SQLAlchemy
Flask-SocketIO
SQLite (banco de dados)
Jinja2 (templates HTML)
QR Code (biblioteca qrcode)
Docker (opcional para ambiente isolado)
📂 Estrutura do Projeto
php
Copiar
Editar
src/
│── config/
│   ├── app_factory.py      # Configuração e criação do app Flask
│   ├── settings.py         # Configurações gerais do projeto
│── extensions.py           # Inicialização de extensões (db, socketio)
│── models/
│   ├── payment.py          # Modelo de pagamento (SQLAlchemy)
│── services/
│   ├── pix_service.py      # Lógica de geração de QR Code PIX
│── routers/
│   ├── payment_routes.py   # Rotas relacionadas a pagamentos
│── templates/              # Arquivos HTML do Flask
│── static/                 # Arquivos estáticos (CSS, JS, imagens)
│── app.py                  # Ponto de entrada do aplicativo
│── requirements.txt        # Dependências do projeto
│── README.md               # Documentação do projeto
│── .env.example            # Exemplo de arquivo de variáveis de ambiente
│── docker-compose.yml      # Configuração para rodar o projeto com Docker (opcional)
📥 Instalação e Execução
1️⃣ Pré-requisitos
Antes de começar, certifique-se de ter instalado:
✅ Python 3.10+
✅ Virtualenv (opcional)
✅ Docker (caso queira rodar via container)

2️⃣ Clonar o repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/real-time-payment-app.git
cd real-time-payment-app
3️⃣ Criar ambiente virtual
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
4️⃣ Instalar dependências
bash
Copiar
Editar
pip install -r requirements.txt
5️⃣ Executar a aplicação
bash
Copiar
Editar
python app.py
A aplicação estará disponível em http://127.0.0.1:5000.

⚡ Uso da API
🔹 Criar um pagamento
bash
Copiar
Editar
GET /payments/pix/<payment_id>
Retorna um QR Code para pagamento.

🔹 Verificar status do pagamento
Após o pagamento, a página é atualizada automaticamente via WebSocket.

🐳 Rodando com Docker
Caso prefira rodar via Docker:

bash
Copiar
Editar
docker-compose up --build
Isso irá iniciar a aplicação e um banco SQLite.

📌 Melhorias Futuras
 Implementação de um banco de dados mais robusto (PostgreSQL)
 Integração com uma API de pagamentos real
 Interface mais amigável para o usuário
👨‍💻 Autor
📌 Seu Nome
📧 seu-email@email.com
🚀 LinkedIn

=======
# 💰 Real-Time Payment App

Aplicação Flask para pagamentos via PIX em tempo real, utilizando WebSockets.

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-SocketIO
- SQLite
- Jinja2 (templates)
- qrcode (geração de QR Code)

## 📥 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/real-time-payment-app.git
   cd real-time-payment-app

   Crie um ambiente virtual:
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

   Instale as dependências:
   pip install -r requirements.txt
   
   Execute a aplicação:
   python app.py
   Acesse em http://127.0.0.1:5000
   
## ⚡ Uso

1. Criar um pagamento:
GET /payments/pix/<payment_id>

2. WebSocket: Atualiza o status do pagamento em tempo real.

## 📌 Melhorias Futuras

 Banco de dados PostgreSQL
 Integração com API de pagamentos

## 📌 Autor: Leandro Souza
📧 leandrosouzaf30@gmail.com | 
🚀 LinkedIn: linkedin.com/in/fleandrosouza
>>>>>>> b9943c43afed576aae67b25b9361dd306e04effa
