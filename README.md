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
- Docker
- Kubernetes
- Kind
- Ingress NGINX

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

## Configurações Kubernetes
Estrutura
   ```
   - k8s/
      config/
         config.yaml
      manifest/
         deployment.yaml
         service.yaml
         ingress.yaml
   
   ```
Arquivos

   * config.yaml: Configuração do cluster Kubernetes utilizando kind.
   * deployment.yaml: Manifesto do Deployment para a aplicação.
   * service.yaml: Configuração do Service para expor a aplicação dentro do cluster.
   * ingress.yaml: Regras de Ingress para expor a aplicação externamente. 

Configuração ambiente de desenvolvimento

1. Criar o Cluster Kubernetes com kind
Certifique-se de ter o kind instalado e execute o seguinte comando, ver documentação [kind](https://kind.sigs.k8s.io/). 
```bash
kind create cluster --config=k8s/config/config.yaml
kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
kubectl wait --namespace ingress-nginx \
	--for=condition=ready pod \
	--selector=app.kubernetes.io/component=controller \
	--timeout=270s
```
2. Realizar build da imagem Docker
```bash
docker build -t <imagem>:latest .
kind load docker-image <imagem>:latest #Esse passo será necessário caso sua imagem esteja local
```
3. Aplicar os Manifestos do Kubernetes
```bash
kubectl apply -f  k8s/manifest/deployment.yaml
kubectl apply -f  k8s/manifest/service.yaml
kubectl apply -f  k8s/manifest/ingress.yaml 
```
4. Testar a Aplicação
Após a configuração, a aplicação estará disponível no domínio api.localhost.com.
   * Agora, a aplicação pode ser acessada via:
   ```bash
   curl localhost/hello -H "Host: api.localhost.com" 
   ```

## Deploy
   1. Criar um novo pipeline no Azure DevOps
      * Acesse o Azure DevOps (https://dev.azure.com/).

      * Selecione seu projeto ou crie um novo.

      * Vá para Pipelines > New pipeline.

      * Escolha a opção GitHub.

      * Autorize o Azure DevOps a acessar seu repositório do GitHub.

      * Selecione o repositório onde está seu código.

   2. Criar o arquivo de pipeline (azure-pipelines.yml)
      * Dentro do repositório no GitHub, crie um arquivo chamado azure-pipelines.yml na raiz do projeto com o seguinte conteúdo:

      * Pipeline para Build e Push da Imagem Docker
      ```bash
      trigger:
      - main

      resources:
      - repo: self

      variables:
      tag: '$(Build.BuildId)'
      azureSubscription: ''  # Substitua pelo nome correto da sua conexão de serviço
      appName: ''  # Nome do seu Azure App Service
      imageName: '$(Build.SourcesDirectory)/Dockerfile'  # Caminho para o seu Dockerfile

      stages:
      - stage: Build
      displayName: Build image
      jobs:
      - job: Build
         displayName: Build
         pool:
            vmImage: ubuntu-latest
         steps:
         - task: Docker@2
            displayName: Build Docker image
            inputs:
            command: build
            dockerfile: '$(Build.SourcesDirectory)/Dockerfile'
            tags: |
               $(tag)

      - stage: Deploy
      displayName: Deploy to Azure
      jobs:
      - job: Deploy
         displayName: Deploy
         pool:
            vmImage: ubuntu-latest
         steps:
         - task: Docker@2  # Corrigido para a versão 2 do task AzureWebAppContainer
            displayName: Deploy Docker container to Azure App Service
            inputs:
            azureSubscription: $(azureSubscription)  # Nome da conexão de serviço
            appName: $(appName)  # Nome do seu App Service
            imageName: $(tag)  # Nome da imagem que foi construída
            isMultiContainer: false  # Se for um container único, defina como false

      ```
      * Agora todo push para a branch "main" ou para a branch que indicar sera rodado o pipeline.

## 📌 Melhorias Futuras
   * Banco de dados PostgreSQL e MongoDB
   * Integração com API de pagamentos

## 📌 Autor: Leandro Souza
   * 📧 leandrosouzaf30@gmail.com 
   * 🚀 Linkedin: [fleandrosouza](linkedin.com/in/fleandrosouza)
