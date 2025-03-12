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
