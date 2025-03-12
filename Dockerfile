FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos necessários
COPY requirements.txt ./

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY src/ ./src

# Expor a porta do Flask (ajuste conforme necessário)
EXPOSE 5000

# Definir variável de ambiente para o Flask
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para rodar a aplicação
CMD ["flask", "run"]