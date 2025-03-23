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
      ```json
      Rota: POST /payments/pix
      Requisicao:
      {
      "value": 100.50
      }

      Resposta (201 Created):
      {
         "message": "The payment has been created",
         "payment": {
            "id": 1,
            "value": 100.50,
            "qr_code": "link_para_qr_code"
         }
      }

      Erros possiveis:
      400 Bad Request: Caso o campo value nao seja enviado.

   2. Obter imagem do QR Code
      ```json
      Rota: GET /payments/pix/qr_code/<file_name>

      Descricao: Retorna a imagem do QR Code associada a um pagamento.

      Parametro na URL: file_name (Nome do arquivo de QR Code)

      Resposta: Retorna a imagem do QR Code (image/png).

      Exemplo de uso:

      GET /payments/pix/qr_code/12345
   
   3. Confirmar pagamento PIX
      ```json
      Rota: POST /payments/pix/confirmation
      Descricao: Confirma um pagamento PIX previamente criado.
      Requisicao:
      {
      "bank_payment_id": 1,
      "value": 100.50
      }

      Resposta (200 OK):

      {
      "message": "The payment has been confirmed"
      }

      Erros possiveis:
      400 Bad Request: Caso bank_payment_id ou value nao sejam enviados.
      404 Not Found: Caso o pagamento nao seja encontrado ou seja invalido.

   4. Obter pagina do pagamento PIX
      ```json
      Rota: GET /payments/pix/<int:payment_id>
      Descricao: Retorna a pagina HTML do pagamento, podendo ser a pagina de confirmacao ou a pagina do QR Code.
      Parametro na URL: payment_id (ID do pagamento)

      Respostas possiveis:
      Se o pagamento for encontrado e ja estiver pago: Retorna a pagina confirmed_payment.html.
      Se o pagamento for encontrado, mas ainda nao pago: Retorna a pagina payment.html contendo as informacoes do QR Code.
      Se o pagamento nao for encontrado: Retorna a pagina 404.html.

## WebSocket: Atualiza o status do pagamento em tempo real.
A aplicacao utiliza WebSockets para atualizar o status do pagamento em tempo real. Assim que o pagamento for confirmado, os usuarios recebem a atualizacao instantaneamente na interface.

## 📌 Melhorias Futuras
 Banco de dados PostgreSQL e MongoDB
 Integração com API de pagamentos

## 📌 Autor: Leandro Souza
📧 leandrosouzaf30@gmail.com | 
🚀 LinkedIn: linkedin.com/in/fleandrosouza
